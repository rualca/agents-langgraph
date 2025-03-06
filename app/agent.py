from typing import Literal, TypedDict
from langgraph.graph import StateGraph, START, END

# Define the state of the agent
class State(TypedDict):
    name: str
    age: int

# Define nodes
# Each node is a function that takes the current state and returns the updated state
def node_1(state: State) -> State:
    state['name'] = 'Alice'
    state['age'] = 25
    return state

def node_2(state: State) -> State:
    state['age'] = 30
    return state

def node_3(state: State) -> State:
    state['name'] = 'Bob'
    return state

# Define the decision node
# The decision node is a function that takes the current state and returns the next node evaluating a condition
def decide_node(state: State) -> Literal['node_2', 'node_3']:
    if state['age'] < 30:
        return 'node_2'
    else:
        return 'node_3'

# Define the graph
builder = StateGraph(State)

builder.add_node('node_1', node_1)
builder.add_node('node_2', node_2)
builder.add_node('node_3', node_3)

builder.add_edge(START, 'node_1')
builder.add_conditional_edges('node_1', decide_node)
builder.add_edge('node_2', END)
builder.add_edge('node_3', END)

graph = builder.compile()