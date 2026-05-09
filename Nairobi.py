# ============================================================
# CCS 2226 Foundations of AI - 2026
# Task Two (b): Map Colouring - Nairobi Sub-Counties
#
# The problem: Colour all 17 Nairobi sub-counties using the
# LEAST number of colours so that no two neighbouring
# sub-counties share the same colour.
#
# We start by trying just 2 colours, then 3, then 4...
# and stop as soon as we find one that works.
# ============================================================


# --- Nairobi's 17 sub-counties and their neighbours ---
# (based on actual geographic adjacency on the Nairobi map)
NEIGHBOURS = {
    "Westlands":         ["Parklands", "Kasarani", "Starehe", "Dagoretti North"],
    "Parklands":         ["Westlands", "Starehe", "Langata"],
    "Kasarani":          ["Westlands", "Roysambu", "Ruaraka", "Mathare"],
    "Roysambu":          ["Kasarani", "Ruaraka", "Mathare"],
    "Ruaraka":           ["Kasarani", "Roysambu", "Embakasi North", "Embakasi West"],
    "Embakasi North":    ["Ruaraka", "Embakasi West", "Embakasi Central"],
    "Embakasi West":     ["Ruaraka", "Embakasi North", "Embakasi Central", "Makadara"],
    "Embakasi Central":  ["Embakasi North", "Embakasi West", "Embakasi East"],
    "Embakasi East":     ["Embakasi Central", "Embakasi South"],
    "Embakasi South":    ["Embakasi East", "Makadara", "Langata"],
    "Makadara":          ["Embakasi West", "Embakasi South", "Starehe", "Langata"],
    "Starehe":           ["Westlands", "Parklands", "Makadara", "Langata", "Mathare"],
    "Langata":           ["Parklands", "Starehe", "Makadara", "Embakasi South", "Kibra", "Dagoretti South"],
    "Kibra":             ["Langata", "Dagoretti North", "Dagoretti South"],
    "Dagoretti North":   ["Westlands", "Kibra", "Dagoretti South"],
    "Dagoretti South":   ["Dagoretti North", "Kibra", "Langata"],
    "Mathare":           ["Kasarani", "Roysambu", "Starehe"],
}

REGIONS = list(NEIGHBOURS.keys())


# --- Check if a colour choice causes any clashes ---
def colour_is_ok(region, colour, current_choices):
    for neighbour in NEIGHBOURS[region]:
        if neighbour in current_choices:
            if current_choices[neighbour] == colour:
                return False  # Neighbour already has this colour!
    return True


# --- Try to colour all regions using the given list of colours ---
# Uses backtracking: try a colour, move on, backtrack if stuck
def solve(current_choices, colours):

    # All regions coloured - we're done!
    if len(current_choices) == len(REGIONS):
        return current_choices

    # Pick the next uncoloured region
    next_region = next(r for r in REGIONS if r not in current_choices)

    for colour in colours:
        if colour_is_ok(next_region, colour, current_choices):
            current_choices[next_region] = colour
            result = solve(current_choices, colours)

            if result:
                return result  # Solution found!

            del current_choices[next_region]  # Backtrack

    return None  # No colour worked - go back further


# --- Find the minimum number of colours needed ---
def find_minimum_colours():
    # Keep trying with more colours until it works
    for num_colours in range(2, 6):
        colours = ["Red", "Blue", "Green", "Yellow", "Purple"][:num_colours]
        result = solve({}, colours)

        if result:
            return num_colours, colours, result

    return None, None, None


# --- Run everything and display the results ---
def main():
    print("=" * 50)
    print("  Nairobi Sub-County Map Colouring - CSP Solver")
    print("=" * 50)
    print("\n  Finding the minimum colours needed...")

    num_colours, colours, solution = find_minimum_colours()

    if solution:
        print(f"\n  Minimum colours needed: {num_colours} ({', '.join(colours)})\n")
        print(f"  {'Sub-County':<22} {'Colour'}")
        print("  " + "-" * 34)
        for region in REGIONS:
            print(f"  {region:<22} {solution[region]}")

        # Verify no two neighbours share a colour
        print("\n  Checking all shared borders...")
        all_good = True
        for region in REGIONS:
            for neighbour in NEIGHBOURS[region]:
                if solution[region] == solution[neighbour]:
                    print(f"  X Clash: {region} and {neighbour} are both {solution[region]}!")
                    all_good = False

        if all_good:
            print(f"  All good! {num_colours} colours is enough for all 17 sub-counties.")
    else:
        print("  Could not find a solution.")

    print("=" * 50)


if __name__ == "__main__":
    main()