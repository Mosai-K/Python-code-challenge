import sys, os

def calculate_rank(inputData):
  """
  input:
  Takes an input text file of team scores and calculates the rank of the data
  for each team.

  output:
  prints team scores according to rank, in descending order.
  """
  rank = {}
  for line in inputData:

    line_strip = line.strip()
    item = line_strip.split(", ")

    team, score = " ".join(item[0].split()[:-1]), int(item[0].split()[-1])
    team1, score1 = " ".join(item[1].split()[:-1]), int(item[1].split()[-1])

    if team not in rank:
      rank[team] = 0
    if team1 not in rank:
      rank[team1] = 0

    if score > score1:
      rank[team] += 3
    elif score < score1:
      rank[team1] += 3
    elif score == score1:
      rank[team1] += 1
      rank[team] += 1
  return rank

def sort_team_ranks(rank):
  order_teams = sorted(rank.items(), key=lambda item: (-item[1], item[0]))
  return order_teams

def format_ranking_results(order_teams):
  output = []
  points = ""
  current_rank = 0
  last_point = None
  for i, (team, score) in enumerate(order_teams, start = 1):
    points = "pts" if score !=  1 else "pt"
    if score != last_point:
      current_rank = i
    output.append(f"{current_rank}. {team}: {score} {points}")
    last_point = score
  return "\n".join(output)

file_path = 'file.txt'
def main():
  with open(file_path, "r") as file:
    lines = file.readlines()
    rankings = calculate_rank(lines)
    print(format_ranking_results(sort_team_ranks(rankings)))
    
if __name__ == "__main__":
    main()