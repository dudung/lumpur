def create_grid(rows, cols, val=0):
    """
    Create grid
    
    Args:
        rows: Number of rows.
        cols: Number of columns.
        val: Value for all cells.
    """
    m = []
    for r in range(rows):
        a_row = []
        for c in range(cols):
            a_row.append(val)
        m.append(a_row)
    return m


def str_grid(grid, char_map=None):
    """
    Generate string representation of the grid customized with char_map.
    
    Args:
    -----
    grid : list of list of int
        A 2D list (grid) containing numerical values.
    
    char_map : dict, optional
        A dictionary mapping numerical values to their characters representation. If not provided, a default mapping will be used for values 0-9 (mapped to '0'-'9'), 10-35 (mapped to 'A'-'Z'), and others mapped to '#'.
    
    Returns:
    --------
    str
        A single string representing the grid with rows separated by newlines. Each cell is represented by a single character according to the `char_map` mapping.
    """
    if char_map is None:
        char_map = {}
    
    def default_mapping(value):
        if 0 <= value <= 9:
            return str(value)
        elif 10 <= value <= 35:
            return chr(ord('A') + value - 10)
        else:
            return '#'

    lines = []
    for row in grid:
        line = []
        for value in row:
            c = char_map.get(value, default_mapping(value))
            line.append(c)
            
        lines.append(''.join(line))
    
    result = '\n'.join(lines)
    return result
