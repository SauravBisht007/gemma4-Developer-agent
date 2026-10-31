from agent.core import GemmaSWEAgent

def main():
    agent = GemmaSWEAgent()
    task = "Fix division-by-zero vulnerability in metric calculation function."
    agent.run_turn(task)

if __name__ == "__main__":
    main()