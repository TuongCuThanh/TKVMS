from collections import namedtuple

# Define the transistor structure
Transistor = namedtuple('Transistor', ['id', 'points'])

# Define the link structure
Link = namedtuple('Link', ['point', 'position'])

# Function to extract points from the transistors
def transistor_points(transistor):
    return transistor.points

# Function to extract the ID from the transistor
def transistor_id(transistor):
    return transistor.id

# Function to flatten a list of lists
def flatten(lst):
    return [item for sublist in lst for item in sublist]

# Function to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# Function to create a link
def make_link(point, position):
    return Link(point, position)

# Function to create a transistor
def make_transistor(id, points):
    return Transistor(id, points)

# Function to swap elements in a list
def list_swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst

# Function to find the index of an element in a list
def index_of(lst, x):
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1

# Function to filter transistors by ID
def filter_transistor(id, g):
    for transistor in g:
        if transistor.id == id:
            return transistor
    return None

# Function to extract nodes from transistors
def nodes(pud, pdn):
    nodes_pud = remove_duplicates(flatten(map(transistor_points, pud)))
    nodes_pdn = remove_duplicates(flatten(map(transistor_points, pdn)))
    return nodes_pud, nodes_pdn

# Function to reorder points
def points(pud, pdn):
    ordem = ('S', 'D')  # Define the order

    # Extract unique points from transistors
    pud_names = remove_duplicates(flatten(map(transistor_points, pud)))
    pdn_names = remove_duplicates(flatten(map(transistor_points, pdn)))

    # Function to reorder points
    def reorder_points(transistors, names):
        links = []
        for point in names:
            for transistor in transistors:
                id, (point1, point2) = transistor
                if point1 == point:
                    links.append((id, ordem[0]))
                elif point2 == point:
                    links.append((id, ordem[1]))
        return links

    # Reorder points for PUD
    points_pud = [make_link(point, reorder_points(pud, pud_names)) for point in pud_names]

    # Reorder points for PDN
    points_pdn = [make_link(point, reorder_points(pdn, pdn_names)) for point in pdn_names]

    return points_pud, points_pdn

# Define the tests
# pud e pdn tests - A(D + E) + BC
pud = [make_transistor('A', ('P2', 'Vdd')), make_transistor('D', ('P1', 'Vdd')),
       make_transistor('E', ('P2', 'P1')), make_transistor('B', ('Out', 'P2')),
       make_transistor('C', ('Out', 'P2'))]
pdn = [make_transistor('A', ('Out', 'P3')), make_transistor('D', ('P3', 'Vss')),
       make_transistor('E', ('P3', 'Vss')), make_transistor('B', ('Out', 'P4')),
       make_transistor('C', ('P4', 'Vss'))]

# pud2 pdn2 - AB + E + CD
pud2 = [make_transistor('A', ('P1', 'Vdd')), make_transistor('B', ('P1', 'Vdd')),
        make_transistor('E', ('P2', 'P1')), make_transistor('D', ('Out', 'P2')),
        make_transistor('C', ('Out', 'P2'))]
pdn2 = [make_transistor('A', ('Out', 'P3')), make_transistor('B', ('P3', 'Vss')),
        make_transistor('E', ('Out', 'Vss')), make_transistor('D', ('Out', 'P4')),
        make_transistor('C', ('P4', 'Vss'))]

# pud3 pdn3 - ABC + DE
pud3 = [make_transistor('A', ('P1', 'Vdd')), make_transistor('B', ('P1', 'Vdd')),
        make_transistor('C', ('P1', 'Vdd')), make_transistor('D', ('Out', 'P1')),
        make_transistor('E', ('Out', 'P1'))]
pdn3 = [make_transistor('A', ('Out', 'P2')), make_transistor('B', ('P2', 'P3')),
        make_transistor('C', ('P3', 'Vss')), make_transistor('D', ('P4', 'Vss')),
        make_transistor('E', ('Out', 'P4'))]


# Function to display PUD and PDN outputs
def display_outputs(pud3, pdn3):
    print("PUD Outputs:")
    for transistor in pud3:
        print(f"Transistor ID: {transistor.id}, Points: {transistor.points}")
    
    print("\nPDN Outputs:")
    for transistor in pdn3:
        print(f"Transistor ID: {transistor.id}, Points: {transistor.points}")

# Display outputs
display_outputs(pud3, pdn3)