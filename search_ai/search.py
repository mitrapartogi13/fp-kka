# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    # Menggunakan Stack dari util.py sesuai instruksi
    # Stack = LIFO (Last In, First Out) -> Karakteristik DFS
    fringe = util.Stack()

    # Masukkan state awal ke dalam fringe.
    # Format data: (state_saat_ini, daftar_aksi_menuju_state_ini)
    fringe.push((problem.getStartState(), []))

    # Set untuk melacak state yang sudah dikunjungi (Graph Search)
    # Ini penting untuk mencegah Pacman bolak-balik di tempat yang sama
    visited = set()

    while not fringe.isEmpty():
        # Ambil elemen paling atas dari Stack (node terdalam yang baru ditambahkan)
        current_state, actions = fringe.pop()

        # Jika state ini adalah tujuan (Goal), kembalikan daftar aksinya
        if problem.isGoalState(current_state):
            return actions

        # Jika state belum pernah dikunjungi, tandai dan cari successor-nya
        if current_state not in visited:
            visited.add(current_state)

            # Dapatkan node tetangga (successors)
            # getSuccessors mengembalikan list of (successor, action, stepCost)
            successors = problem.getSuccessors(current_state)

            for next_state, action, cost in successors:
                # Tambahkan state tetangga ke Stack dengan jalur yang diperbarui
                # Kita membuat list baru (actions + [action]) agar path tiap node unik
                new_actions = actions + [action]
                fringe.push((next_state, new_actions))

    # Kembalikan list kosong jika solusi tidak ditemukan
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    
    # BFS menggunakan Queue (FIFO) agar mengekspansi level demi level
    from util import Queue
    fringe = Queue()

    # Masukkan state awal: (state, daftar_aksi)
    start_state = problem.getStartState()
    fringe.push((start_state, []))

    # List untuk melacak state yang sudah dikunjungi
    visited = []

    while not fringe.isEmpty():
        current_state, actions = fringe.pop()

        # Jika sudah sampai tujuan, kembalikan jalurnya
        if problem.isGoalState(current_state):
            return actions

        # Logika Graph Search: cek apakah state sudah pernah dikunjungi
        if current_state not in visited:
            visited.append(current_state)

            successors = problem.getSuccessors(current_state)
            for next_state, action, cost in successors:
                # Tambahkan ke antrean jika belum dikunjungi
                if next_state not in visited:
                    new_actions = actions + [action]
                    fringe.push((next_state, new_actions))

    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    
    # Gunakan PriorityQueue agar node dengan cost terendah diekspansi duluan
    from util import PriorityQueue
    fringe = PriorityQueue()

    # Format data dalam fringe: (state, list_aksi, total_biaya_sejauh_ini)
    # Argumen ke-2 pada push adalah prioritas (total_biaya)
    start_state = problem.getStartState()
    fringe.push((start_state, [], 0), 0)

    visited = set()

    while not fringe.isEmpty():
        # Pop akan mengembalikan item dengan prioritas (cost) terendah
        current_state, actions, current_cost = fringe.pop()

        # Cek tujuan
        if problem.isGoalState(current_state):
            return actions

        # Jika belum dikunjungi, proses
        if current_state not in visited:
            visited.add(current_state)

            successors = problem.getSuccessors(current_state)
            for next_state, action, step_cost in successors:
                if next_state not in visited:
                    # Hitung biaya kumulatif baru
                    new_cost = current_cost + step_cost
                    new_actions = actions + [action]
                    
                    # Push ke PQ dengan prioritas = new_cost
                    fringe.push((next_state, new_actions, new_cost), new_cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first.

    Standard A* implementation using the project's PriorityQueue from util.py.
    The priority of each fringe item is f(n) = g(n) + h(n), where g(n) is the
    path cost from the start to n, and h(n) is the heuristic estimate from n
    to the goal.
    """

    from util import PriorityQueue

    start = problem.getStartState()
    fringe = PriorityQueue()
    # Each item: (state, actions_so_far, g_cost)
    fringe.push((start, [], 0), heuristic(start, problem))

    # Track best known g-cost for each visited state to avoid re-expanding with higher cost
    best_g = {}

    while not fringe.isEmpty():
        state, actions, g_cost = fringe.pop()

        # If we've already seen a cheaper path to this state, skip it
        if state in best_g and best_g[state] <= g_cost:
            continue

        best_g[state] = g_cost

        if problem.isGoalState(state):
            return actions

        for successor, action, step_cost in problem.getSuccessors(state):
            new_g = g_cost + step_cost
            f = new_g + heuristic(successor, problem)
            fringe.push((successor, actions + [action], new_g), f)

    # No solution found
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
