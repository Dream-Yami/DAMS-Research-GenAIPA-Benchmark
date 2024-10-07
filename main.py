from experiments import run

if __name__ == "__main__":
    print("Running list of policy Documents")
    
    policyList = ["Uber"]
    for i in range(len(policyList)):
        print("Starting:",policyList[i])
        run(policyList[i])
        print("Finished:",policyList[i])