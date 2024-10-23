def flatten(lst: list, depth: int | None = None) -> list:
    result = []
    if depth is None:
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else: 
                result.append(item)
        return result
    
    for item in lst:
        if isinstance(item, list) and depth > 0:
            result.extend(flatten(item, depth=depth - 1))
        else:
            result.append(item)
    return result