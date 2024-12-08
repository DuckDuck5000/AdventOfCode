# Python Script to Filter Data and Calculate Percentiles

# Define your data
data = {
    "2023": [
        {"Day": 16, "Part1_Rank": 875, "Part2_Rank": 1618},
        {"Day": 15, "Part1_Rank": 2244, "Part2_Rank": 581},
        {"Day": 14, "Part1_Rank": 6384, "Part2_Rank": 2465},
        {"Day": 13, "Part1_Rank": 2405, "Part2_Rank": 2131},
        {"Day": 12, "Part1_Rank": 537, "Part2_Rank": 876},
        {"Day": 11, "Part1_Rank": 484, "Part2_Rank": 337},
        {"Day": 10, "Part1_Rank": 2592, "Part2_Rank": 256},
        {"Day": 9, "Part1_Rank": 331, "Part2_Rank": 985},
        {"Day": 8, "Part1_Rank": 8343, "Part2_Rank": 2792},
        {"Day": 7, "Part1_Rank": 2494, "Part2_Rank": 2711},
        {"Day": 6, "Part1_Rank": 18, "Part2_Rank": 2339},
        {"Day": 5, "Part1_Rank": 3245, "Part2_Rank": 1784},
        {"Day": 4, "Part1_Rank": 3897, "Part2_Rank": 1165},
        {"Day": 3, "Part1_Rank": 1624, "Part2_Rank": 1736},
        {"Day": 2, "Part1_Rank": 624, "Part2_Rank": 2784},
        {"Day": 1, "Part1_Rank": 4080, "Part2_Rank": 1197},
    ],
    "2022": [
        {"Day": 25, "Part1_Rank": 12630, "Part2_Rank": 7951},
        {"Day": 24, "Part1_Rank": 7881, "Part2_Rank": 7565},
        {"Day": 23, "Part1_Rank": 12514, "Part2_Rank": 12269},
        {"Day": 22, "Part1_Rank": 14679, "Part2_Rank": 9460},
        {"Day": 21, "Part1_Rank": 14725, "Part2_Rank": 11430},
        {"Day": 20, "Part1_Rank": 14698, "Part2_Rank": 13814},
        {"Day": 19, "Part1_Rank": 11243, "Part2_Rank": 10213},
        {"Day": 18, "Part1_Rank": 17986, "Part2_Rank": 14119},
        {"Day": 17, "Part1_Rank": 20544, "Part2_Rank": 14932},
        {"Day": 16, "Part1_Rank": 23056, "Part2_Rank": 17760},
        {"Day": 15, "Part1_Rank": 33239, "Part2_Rank": 28759},
        {"Day": 14, "Part1_Rank": 21064, "Part2_Rank": 19572},
        {"Day": 13, "Part1_Rank": 33706, "Part2_Rank": 32627},
        {"Day": 12, "Part1_Rank": 21792, "Part2_Rank": 20716},
        {"Day": 11, "Part1_Rank": 7126, "Part2_Rank": 3586},
        {"Day": 10, "Part1_Rank": 5476, "Part2_Rank": 3879},
        {"Day": 9, "Part1_Rank": 2577, "Part2_Rank": 1791},
        {"Day": 8, "Part1_Rank": 3450, "Part2_Rank": 1327},
        {"Day": 7, "Part1_Rank": 591, "Part2_Rank": 385},
        {"Day": 6, "Part1_Rank": 5543, "Part2_Rank": 4190},
        {"Day": 5, "Part1_Rank": 1572, "Part2_Rank": 1003},
        {"Day": 4, "Part1_Rank": 8994, "Part2_Rank": 6788},
        {"Day": 3, "Part1_Rank": 6510, "Part2_Rank": 8345},
        {"Day": 2, "Part1_Rank": 689, "Part2_Rank": 3250},
        {"Day": 1, "Part1_Rank": 2606, "Part2_Rank": 2018},
    ],
    "2024": [
        {"Day": 7, "Part1_Rank": 46096, "Part2_Rank": 43205},
        {"Day": 6, "Part1_Rank": 481, "Part2_Rank": 1533},
        {"Day": 5, "Part1_Rank": 387, "Part2_Rank": 367},
        {"Day": 4, "Part1_Rank": 3486, "Part2_Rank": 2644},
        {"Day": 3, "Part1_Rank": 1218, "Part2_Rank": 1991},
        {"Day": 2, "Part1_Rank": 3329, "Part2_Rank": 1682},
        {"Day": 1, "Part1_Rank": 13312, "Part2_Rank": 12599},
    ]
}

# Number of participants per year
participants = {
    "2022": 300000,
    "2023": 255000,
    "2024": 200000
}

def filter_and_calculate_percentiles(data, participants, rank_threshold):
    """
    Filters the data based on rank thresholds and calculates percentiles.

    Args:
        data (dict): Dictionary with years as keys and list of day data as values.
        participants (dict): Dictionary with years as keys and number of participants as values.
        rank_threshold (int): The maximum rank to include.

    Returns:
        dict: Dictionary with years as keys and list of filtered day data including percentiles.
    """
    result = {}
    for year, entries in data.items():
        total_participants = participants.get(year, 0)
        if total_participants == 0:
            continue  # Skip if participant data is missing

        # Filter entries where both Part1_Rank and Part2_Rank <= rank_threshold
        filtered = [
            entry for entry in entries
            if entry["Part1_Rank"] <= rank_threshold and entry["Part2_Rank"] <= rank_threshold
        ]

        if not filtered:
            continue  # No qualifying entries for this year

        # Calculate percentiles
        for entry in filtered:
            part1_percentile = (1 - (entry["Part1_Rank"] / total_participants)) * 100
            part2_percentile = (1 - (entry["Part2_Rank"] / total_participants)) * 100
            entry["Part1_Percentile"] = f"{part1_percentile:.2f}%"
            entry["Part2_Percentile"] = f"{part2_percentile:.2f}%"

        result[year] = filtered

    return result

def generate_markdown(filtered_data, participants):
    """
    Generates Markdown tables from the filtered data.

    Args:
        filtered_data (dict): Dictionary with years as keys and list of day data including percentiles.
        participants (dict): Dictionary with years as keys and number of participants as values.

    Returns:
        str: Formatted Markdown string.
    """
    markdown = ""
    for year in sorted(filtered_data.keys(), reverse=True):
        entries = filtered_data[year]
        total_participants = participants.get(year, "Unknown")

        # Header for the year
        markdown += f"## {year} ({total_participants:,} Participants)\n\n"

        # Table header
        markdown += "| Day | Part 1 Rank | Part 1 Percentile | Part 2 Rank | Part 2 Percentile |\n"
        markdown += "|-----|-------------|-------------------|-------------|-------------------|\n"

        # Table rows
        for entry in sorted(entries, key=lambda x: x["Day"]):
            day = entry["Day"]
            part1_rank = entry["Part1_Rank"]
            part1_percentile = entry["Part1_Percentile"]
            part2_rank = entry["Part2_Rank"]
            part2_percentile = entry["Part2_Percentile"]
            markdown += f"| {day}   | {part1_rank}       | {part1_percentile}            | {part2_rank}       | {part2_percentile}            |\n"

        # Separator
        markdown += "\n---\n\n"

    return markdown

# Process the data
filtered_data = filter_and_calculate_percentiles(data, participants, rank_threshold=10000)

# Generate Markdown
markdown_output = generate_markdown(filtered_data, participants)

# Print the Markdown
print(markdown_output)
