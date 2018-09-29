def correct_guess(solution, attempts, proposal):
    if len(proposal) != 1:
        return None
    if proposal in attempts:
        return None
    if proposal in solution:
        return True
    else:
        return False
