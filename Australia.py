# ============================================================
# CCS 2226 Foundations of AI - 2026
# Task Two (a): Map Colouring using Constraint Satisfaction
#
# The problem: Colour Australia's regions using only 3 colours
# (Blue, Red, Green) so that no two neighbouring regions
# share the same colour.
# ============================================================


# --- The 3 colours we're allowed to use ---
COLOURS = ["Blue", "Red", "Green"]

# --- Australia's regions and who they share a border with ---
# Think of this as a list of neighbours for each region
NEIGHBOURS = {
    "WA":  ["NT", "SA"],
    "NT":  ["WA", "SA", "Q"],
    "SA":  ["WA", "NT", "Q", "NSW", "V"],
    "Q":   ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V":   ["SA", "NSW"],
    "TAS": []  # Island - no land borders!
}

REGIONS = list(NEIGHBOURS.keys())


# --- Check if a colour choice is valid ---
# i.e. none of the neighbours already have that colour
def colour_is_ok(region, colour, current_choices):
    for neighbour in NEIGHBOURS[region]:
        if neighbour in current_choices:
            if current_choices[neighbour] == colour:
                return False  # Clash! This colour won't work here
    return True  # All good, no clashes


# --- The main solving function (uses backtracking) ---
# It tries colours one by one. If stuck, it goes back and tries something else.
def solve(current_choices={}):

    # Done! Every region has been coloured
    if len(current_choices) == len(REGIONS):
        return current_choices

    # Pick the next region that hasn't been coloured yet
    next_region = next(r for r in REGIONS if r not in current_choices)

    # Try each colour for this region
    for colour in COLOURS:
        if colour_is_ok(next_region, colour, current_choices):

            # Assign the colour and move on
            current_choices[next_region] = colour
            result = solve(current_choices)

            if result:
                return result  # Found a working solution!

            # That path didn't work - remove the colour and try the next one
            del current_choices[next_region]

    return None  # No colour worked here - go back and try something else


# --- Run the solver and show the result ---
def main():
    print("=" * 45)
    print("  Australia Map Colouring - CSP Solver")
    print("  Colours: Blue, Red, Green")
    print("=" * 45)

    solution = solve()

    if solution:
        print("\n  Here's the colouring that works:\n")
        print(f"  {'Region':<20} {'Colour'}")
        print("  " + "-" * 30)
        for region in REGIONS:
            print(f"  {region:<20} {solution[region]}")

        # Double-check that no two neighbours share a colour
        print("\n  Checking all borders...")
        all_good = True
        for region in REGIONS:
            for neighbour in NEIGHBOURS[region]:
                if solution[region] == solution[neighbour]:
                    print(f"  X Problem: {region} and {neighbour} are both {solution[region]}!")
                    all_good = False

        if all_good:
            print("  All good! No two neighbouring regions share a colour.")
    else:
        print("\n  Couldn't find a solution.")

    print("=" * 45)


if __name__ == "__main__":
    main()