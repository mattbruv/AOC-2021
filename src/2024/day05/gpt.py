
def parse_input(input_data):
    rules_part, updates_part = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in rules_part.splitlines()]
    updates = [list(map(int, line.split(","))) for line in updates_part.splitlines()]
    return rules, updates

def is_valid_update(update, rules):
    # Create a map for the index of each page in the update
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:  # Check if x appears before y
                return False
    return True

def find_middle_sum(input_data):
    rules, updates = parse_input(input_data)
    valid_updates = []
    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update[len(update) // 2])  # Find the middle page
    return sum(valid_updates)

# Example Input
input_data = open("input.txt").read()

# Run the function
result = find_middle_sum(input_data)
print("Result:", result)
