#!/usr/bin/env python3
"""
Bedrock Knowledge Base Search Tool
간단한 CLI 도구로 Bedrock KB에서 정보를 검색합니다.
"""

import os
import sys
import json
import boto3
from botocore.exceptions import ClientError

# AWS Bedrock Configuration
BEDROCK_REGION = os.getenv('AWS_REGION', 'ap-northeast-2')
KNOWLEDGE_BASE_ID = os.getenv('BEDROCK_KB_ID', '6XAPEGURQ3')

# Initialize Bedrock client
bedrock_agent_runtime = boto3.client(
    'bedrock-agent-runtime',
    region_name=BEDROCK_REGION
)


def search_knowledge_base(query: str, num_results: int = 10) -> dict:
    """
    Bedrock Knowledge Base에서 검색을 수행합니다.

    Args:
        query: 검색할 내용
        num_results: 반환할 결과 개수 (기본값: 10)

    Returns:
        검색 결과 딕셔너리
    """
    try:
        response = bedrock_agent_runtime.retrieve(
            knowledgeBaseId=KNOWLEDGE_BASE_ID,
            retrievalQuery={
                'text': query
            },
            retrievalConfiguration={
                'vectorSearchConfiguration': {
                    'numberOfResults': num_results
                }
            }
        )

        results = []
        for idx, result in enumerate(response.get('retrievalResults', []), 1):
            content = result.get('content', {}).get('text', '')
            score = result.get('score', 0)
            location = result.get('location', {})
            source = location.get('s3Location', {}).get('uri', 'Unknown source')

            results.append({
                'rank': idx,
                'score': score,
                'source': source,
                'content': content
            })

        return {
            'success': True,
            'query': query,
            'results_count': len(results),
            'results': results
        }

    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_msg = e.response['Error']['Message']
        return {
            'success': False,
            'error': f"Bedrock 오류 ({error_code}): {error_msg}"
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"검색 중 오류 발생: {str(e)}"
        }


def print_results(results: dict, verbose: bool = False):
    """검색 결과를 출력합니다."""
    if not results['success']:
        print(f"❌ {results['error']}")
        return

    print(f"🔍 검색어: {results['query']}")
    print(f"📊 결과 개수: {results['results_count']}\n")
    print("=" * 80)

    for result in results['results']:
        print(f"\n📄 결과 {result['rank']} (관련도: {result['score']:.2f})")
        print(f"출처: {result['source']}")

        if verbose:
            print(f"\n내용:\n{result['content']}")
        else:
            # 처음 500자만 출력
            content_preview = result['content'][:500]
            if len(result['content']) > 500:
                content_preview += "..."
            print(f"\n내용:\n{content_preview}")

        print("-" * 80)


def main():
    """메인 실행 함수"""
    if len(sys.argv) < 2:
        print("사용법: python search_bedrock_kb.py <검색어> [결과개수] [--verbose]")
        print("\n예시:")
        print("  python search_bedrock_kb.py '채용 프로세스'")
        print("  python search_bedrock_kb.py '평가 기준' 5")
        print("  python search_bedrock_kb.py '회사 가치관' 10 --verbose")
        sys.exit(1)

    query = sys.argv[1]
    num_results = 10
    verbose = False

    # 선택적 인자 파싱
    if len(sys.argv) > 2:
        try:
            num_results = int(sys.argv[2])
        except ValueError:
            if sys.argv[2] == '--verbose':
                verbose = True

    if len(sys.argv) > 3 and sys.argv[3] == '--verbose':
        verbose = True

    # 검색 수행
    results = search_knowledge_base(query, num_results)

    # 결과 출력
    print_results(results, verbose)

    # JSON으로도 저장 (선택사항)
    output_file = f"bedrock_search_{query.replace(' ', '_')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n💾 결과가 {output_file}에 저장되었습니다.")


if __name__ == "__main__":
    main()
