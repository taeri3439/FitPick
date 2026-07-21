"""파이프라인 그래프 조립 스모크 테스트."""

from app.graph import build_graph


def test_graph_builds():
    graph = build_graph()
    assert graph is not None
    # TODO: 노드 연결/실행 테스트 추가
