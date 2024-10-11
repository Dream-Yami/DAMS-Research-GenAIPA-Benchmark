from experiments import run, runReg
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "reg":
        regList = ["CCPA", "GDPR"]
        for i in range(len(regList)):
            print("Starting:",regList[i])
            runReg(regList[i])
            print("Finished:",regList[i])
    else:
        policyList = ["Spotify"] #include "AirBnB", "Facebook", "Uber", "Spotify", "Twitter"
        for i in range(len(policyList)):
            print("Starting:",policyList[i])
            run(policyList[i])
            print("Finished:",policyList[i])    