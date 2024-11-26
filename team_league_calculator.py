import re
import sys, os

file_path = "file.txt"

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
    item = line_strip.split(",")

    team, score = " ".join(item[0].strip().split()[:-1]), int(item[0].split()[-1])
    team1, score1 = " ".join(item[1].strip().split()[:-1]), int(item[1].split()[-1])
 
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

  order_teams = sorted(rank.items(), key=lambda item: (-item[1], item[0]))

  for i, (team, points) in enumerate(order_teams, start = 1):
    print(f"{i}. {team}: {points} pts")


def main():
  with open(file_path, "r") as file:
    lines = file.readlines()
    calculate_rank(lines)

if __name__ == "__main__":
    main()