import random 
question = input("Do you want to know about both of the playing teams? (yes/no): ").lower() 
if question == "yes":
    print("""Pakistan is known for producing some of the most fearsome pace attacks in T20 cricket, 
and their bowling often makes them a real threat in limited overs formats. However, their batting has sometimes been 
inconsistent, which affects their stability in crunch matches. Over the years, Pakistan has won several major T20 contests 
but has lagged behind in head-to-head encounters against India. In T20 Internationals, India has dominated the rivalry: 
in the 14 T20Is between them, India has won 10, Pakistan 3, with one match decided via tie/bowl-out. 
Pakistan’s strength lies in their attack and occasional brilliance,
but their inconsistency in batting and fielding has made them a more volatile team under pressure.

India’s T20 side blends stability and firepower in batting, 
with strong middle and lower orders that often rescue innings.
Their spin and pace bowling balance also helps them adapt to different pitch conditions. 
In the head-to-head T20 record versus Pakistan, India holds a clear edge: 10 wins out of 14 matches, with just 3 losses. 
India also recently ended an ICC trophy drought by winning the 2024 T20 World Cup. Because of their more consistent batting, 
disciplined fielding, and match temperament, India is generally viewed as the more stable of the two sides in T20s.""")
else:
    print("")


class Cricket:
    def __init__(self,overs,n_of_players,n_of_balls):
        
        self.overs=overs
        self.n_of_players=n_of_players
        self.n_of_balls=n_of_balls
class TeamA(Cricket):
    def __init__(self,bowling_lineup,batting_lineup,name,n_of_bowlers,n_of_batters,overs,n_of_players,n_of_balls):
        super().__init__(overs,n_of_players,n_of_balls)
        self.name=name
        self.bowling_lineup=bowling_lineup
        self.batting_lineup=batting_lineup
        self.n_of_players=n_of_players
        self.n_of_balls=n_of_balls
        self.batters=n_of_batters
        self.bowlers=n_of_bowlers
    def TeamA_strengths(self,defense,attack,batting_strength,bowling_strength,probability_of_stopping_a_boundary,probability_of_hitting_a_boundary,probability_of_taking_a_wicket):
        self.defense=defense
        self.attack=attack
        self.batting_strength=batting_strength
        self.bowling_strength=bowling_strength
        self.probability_boundary=probability_of_hitting_a_boundary
        self.probability_stopping=probability_of_stopping_a_boundary
        self.probability_wicket=probability_of_taking_a_wicket     
    def TeamA_weaknesses(self,probability_of_dropping_a_catch,probability_of_getting_runout,past_loss_record,record_of_bad_fielding,record_of_bad_batting,unstability_percentage):
        self.probability_dropping=probability_of_dropping_a_catch
        self.probability_runout=probability_of_getting_runout
        self.past_loss=past_loss_record
        self.record_b=record_of_bad_batting
        self.record_f=record_of_bad_fielding
        self.unstability_percentage=unstability_percentage
class TeamB(Cricket):
    def __init__(self,bowling_lineup,batting_lineup,name,n_of_bowlers,n_of_batters,overs,n_of_players,n_of_balls):
        super().__init__(overs,n_of_players,n_of_balls)
        self.name=name
        self.bowling_lineup=bowling_lineup
        self.batting_lineup=batting_lineup
        self.n_of_players=n_of_players
        self.n_of_balls=n_of_balls
        self.batters=n_of_batters
        self.bowlers=n_of_bowlers
    def TeamB_strengths(self,defense,attack,batting_strength,bowling_strength,probability_of_stopping_a_boundary,probability_of_hitting_a_boundary,probability_of_taking_a_wicket):
        self.defense=defense
        self.attack=attack
        self.batting_strength=batting_strength
        self.bowling_strength=bowling_strength
        self.probability_boundary=probability_of_hitting_a_boundary
        self.probability_stopping=probability_of_stopping_a_boundary
        self.probability_wicket=probability_of_taking_a_wicket     
    def TeamB_weaknesses(self,probability_of_dropping_a_catch,probability_of_getting_runout,past_loss_record,record_of_bad_fielding,record_of_bad_batting,unstability_percentage):
        self.probability_dropping=probability_of_dropping_a_catch
        self.probability_runout=probability_of_getting_runout
        self.past_loss=past_loss_record
        self.record_b=record_of_bad_batting
        self.record_f=record_of_bad_fielding
        self.unstability_percentage=unstability_percentage
class Stats:
    
    pakistan = TeamA(
        bowling_lineup=["Shaheen Afridi", "Haris Rauf", "Naseem Shah","Abrar Ahmed","Faheem Ashraf","Mohammad Nawaz"],
        batting_lineup=["Babar Azam", "Mohammad Rizwan", "Saim Ayub","Sahibzada Farhan","Iftikhar Ahmed"],
        name="Pakistan",
        n_of_bowlers=6,
        n_of_batters=5,
        overs=20,
        n_of_players=11,
        n_of_balls=120
    )

    pakistan.TeamA_strengths(
        defense=0.80,
        attack=0.83,
        batting_strength=0.81,
        bowling_strength=0.88,
        probability_of_stopping_a_boundary=0.816,
        probability_of_hitting_a_boundary=0.23,
        probability_of_taking_a_wicket=0.19
    )

    pakistan.TeamA_weaknesses(
        probability_of_dropping_a_catch=0.184,
        probability_of_getting_runout=0.11,
        past_loss_record=0.40,
        record_of_bad_fielding=0.25,
        record_of_bad_batting=0.22,
        unstability_percentage=0.18
    )
    india = TeamB(
        bowling_lineup=["Jasprit Bumrah", "Ravindra Jadeja", "Kuldeep Yadav","Arshdeep Singh","Hardik Pandya"],
        batting_lineup=["Virat Kohli", "Suryakumar Yadav", "Rohit Sharma","Shubman Gill","Tilak Verma","Abhishek Sharma"],
        name="India",
        n_of_bowlers=5,
        n_of_batters=6,
        overs=20,
        n_of_players=11,
        n_of_balls=120
    )
    india.TeamB_strengths(
        defense=0.82,
        attack=0.88,
        batting_strength=0.86,
        bowling_strength=0.82,
        probability_of_stopping_a_boundary=0.83,
        probability_of_hitting_a_boundary=0.26,
        probability_of_taking_a_wicket=0.17
    )

    india.TeamB_weaknesses(
        probability_of_dropping_a_catch=0.12,
        probability_of_getting_runout=0.08,
        past_loss_record=0.25,
        record_of_bad_fielding=0.15,
        record_of_bad_batting=0.18,
        unstability_percentage=0.10
    )
class Match(Cricket):
    def __init__(self, overs, n_of_players, n_of_balls, teamA='Pakistan', teamB='India'):
        super().__init__(overs, n_of_players, n_of_balls)
        self.stats = Stats()
        self.teamA = teamA
        self.teamB = teamB

    def simulate_single_match(self, teamA, teamB, silent=False):
        """Simulates one match and returns the winner."""
        pakistan = self.stats.pakistan
        india = self.stats.india

        if not silent:
            print(f"A slight guess on who will win the match between {teamA} and {teamB}\n")

            print("\n----------- TEAM OVERVIEW -----------\n")

            print(f"{pakistan.name}")
            print("Batting lineup:", ", ".join(pakistan.batting_lineup))
            print("Bowling lineup:", ", ".join(pakistan.bowling_lineup))
            print(f"Defense: {pakistan.defense}")
            print(f"Attack: {pakistan.attack}")
            print(f"Batting strength: {pakistan.batting_strength}")
            print(f"Bowling strength: {pakistan.bowling_strength}")
            print(f"Unstability: {pakistan.unstability_percentage}\n")

            print(f"{india.name} :")
            print("Batting lineup:", ", ".join(india.batting_lineup))
            print("Bowling lineup:", ", ".join(india.bowling_lineup))
            print(f"Defense: {india.defense}")
            print(f"Attack: {india.attack}")
            print(f"Batting strength: {india.batting_strength}")
            print(f"Bowling strength: {india.bowling_strength}")
            print(f"Unstability: {india.unstability_percentage}\n")

            print("-------------------------------------\n")

        # Toss
        toss_winner = random.choice(["Pakistan", "India"])
        decision = random.choice(["bat", "bowl"])
        if not silent:
            print("=== TOSS ===")
            print(f"{toss_winner} won the toss and decided to {decision} first.\n")

        # Who bats/bowls first
        if decision == "bat":
            batting_first = toss_winner
            bowling_first = "India" if toss_winner == "Pakistan" else "Pakistan"
        else:
            bowling_first = toss_winner
            batting_first = "India" if toss_winner == "Pakistan" else "Pakistan"

        if not silent:
            print("-----------'FIRST INNINGS'-------------")
            print(f"Team {batting_first} will bat first and give a target to {bowling_first}.\n")

        runs_first = random.randint(100, 180)
        wickets_first = random.randint(1, 9)

        if not silent:
            print(f"{batting_first} scored {runs_first}/{wickets_first} in 20 overs.")
            print(f"Target for {bowling_first}: {runs_first + 1}\n")

        # Second innings
        if not silent:
            print("---------------'SECOND INNINGS'---------------------")
            print(f"{bowling_first} is now chasing the target.\n")

        if bowling_first == "Pakistan":
            chasing_strength = pakistan.batting_strength
            defending_strength = india.bowling_strength
        else:
            chasing_strength = india.batting_strength
            defending_strength = pakistan.bowling_strength

        win_chance = chasing_strength / (chasing_strength + defending_strength)
        chasing_wins = random.random() < win_chance

        if chasing_wins:
            if not silent:
                runs_second = random.randint(runs_first + 1, runs_first + 6)
                wickets_second = random.randint(2, 8)
                overs_second = random.randint(14, 19)
                balls = random.randint(0, 5)
                print(f"{bowling_first} scored {runs_second}/{wickets_second} in {overs_second}.{balls} overs.")
                print(f"{bowling_first} wins by {10 - wickets_second} wickets!\n")
            return bowling_first
        else:
            if not silent:
                reason = random.choice(["all_out", "overs_done"])
                if reason == "all_out":
                    runs_second = random.randint(runs_first - 30, runs_first - 1)
                    wickets_second = 10
                    print(f"{bowling_first} scored {runs_second}/{wickets_second} (all out).")
                    print(f"{batting_first} wins by {runs_first - runs_second} runs.\n")
                else:
                    runs_second = random.randint(runs_first - 25, runs_first - 1)
                    wickets_second = random.randint(3, 9)
                    print(f"{bowling_first} scored {runs_second}/{wickets_second} in 20 overs(no balls left).")
                    print(f"{batting_first} wins by {runs_first - runs_second} runs.\n")
            return batting_first

    def simulate_many_matches(self, n):
        """Simulates n matches quietly and shows overall win probabilities based on team stats."""

        results = {self.teamA: 0, self.teamB: 0, "Tie": 0}

        pakistan = self.stats.pakistan
        india = self.stats.india


        pakistan_rating = (
            pakistan.defense * 0.25 +
            pakistan.attack * 0.25 +
            pakistan.batting_strength * 0.25 +
            pakistan.bowling_strength * 0.25
        ) * (1 - pakistan.unstability_percentage)

        india_rating = (
            india.defense * 0.25 +
            india.attack * 0.25 +
            india.batting_strength * 0.25 +
            india.bowling_strength * 0.25
        ) * (1 - india.unstability_percentage)


        total_rating = pakistan_rating + india_rating
        pakistan_win_chance = pakistan_rating / total_rating 
        india_win_chance = india_rating / total_rating

        for _ in range(n):

            if random.random() < india_win_chance:
                results[self.teamB] += 1
            else:
                results[self.teamA] += 1
            

        teamA_prob = (results[self.teamA] / n) * 100
        teamB_prob = (results[self.teamB] / n) * 100

        print(f"""\nWith accordance to statistics, India has better overall odds to win than Pakistan
due to their team being stable in each of the areas such as batting, bowling, and 
fielding, while on the other hand Pakistan is highly unstable in many areas. However, 
their pace attack is unmatched, so we can never predict exactly who will win because 
cricket is full of surprises and the victory of a certain team totally depends on how 
the team performs on the match day.\n""")
        

        print(f"\nCalculated chances before simulation:")
        print(f"{self.teamA}: {pakistan_win_chance * 100:.2f}%")
        print(f"{self.teamB}: {india_win_chance * 100:.2f}%\n")

        print(f"\nSimulated {n} T20 Matches between {self.teamA} and {self.teamB}:")
        print(f"{self.teamA} Win Probability: {teamA_prob:.2f}%")
        print(f"{self.teamB} Win Probability: {teamB_prob:.2f}%")

        if teamA_prob > teamB_prob:
            print(f"\n{self.teamA} is more likely to win overall.")
        elif teamB_prob > teamA_prob:
            print(f"\n{self.teamB} is more likely to win overall.")
        else:
            print("\nBoth teams are evenly matched.")

        

match = Match(20,11,120)
match.simulate_single_match("Pakistan","India")
match.simulate_many_matches(1000)
