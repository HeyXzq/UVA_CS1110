# name: Jacquelyn(Ziqi) Xu
# computing ID: gqj3wx

# name the player and the opponent
name_player = str(input("What player would you like to calculate statistics for? "))
name_opponent = str(input("What team was the opponent in the game you would like to calculate statistics for? "))
# 3's attempts and successes
attempt_3 =int(input("How many 3's did " + name_player + " attempt this game? "))
made_3 = int(input("How many 3's did " + name_player + " make this game? "))
# 2's attempts and successes
attempt_2 = int(input("How many 2's did " + name_player + " attempt this game? "))
made_2 = int(input("How many 2's did " + name_player + " make this game? "))
# free throw's attempts and successes
attempt_free = int(input("How many free throws did " + name_player + " attempt this game? "))
made_free = int(input("How many free throws did " + name_player + " make this game? "))


percentage_field = ((made_3 + made_2) / (attempt_3 + attempt_2)) * 100
percentage_free = (made_free / attempt_free) * 100
score = made_3 * 3 + made_2 * 2 + made_free * 1

print(name_player, "had a " + str(percentage_field) + "% field goal percentage and a " + str(percentage_free) + "% free throw percentage")
print(name_player, "scored " + str(score) + " points against " + str(name_opponent) + ". Wahoowa!")