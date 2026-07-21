"""LangGraph 파이프라인 조립.

    condition_parser → candidate_filter → harmony_scorer → recommender

VLM 속성 추출(attribute_extractor)은 확장 단계이므로 기본 그래프에서는 제외.
필요 시 candidate_filter 앞단에 노드로 추가한다.
"""

from langgraph.graph import END, StateGraph

from app.nodes import (
    candidate_filter,
    condition_parser,
    harmony_scorer,
    recommender,
)
from app.state import CodiState


def build_graph() -> StateGraph:
    graph = StateGraph(CodiState)

    graph.add_node("condition_parser", condition_parser)
    graph.add_node("candidate_filter", candidate_filter)
    graph.add_node("harmony_scorer", harmony_scorer)
    graph.add_node("recommender", recommender)

    graph.set_entry_point("condition_parser")
    graph.add_edge("condition_parser", "candidate_filter")
    graph.add_edge("candidate_filter", "harmony_scorer")
    graph.add_edge("harmony_scorer", "recommender")
    graph.add_edge("recommender", END)

    return graph


compiled_graph = build_graph()
