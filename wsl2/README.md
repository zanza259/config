Note: 
Need to store run_wsl2_at_startup.vba at
```
echo "" > $HOME\run_wsl2_at_startup.vbs

```

Then added under the Task Scheduler program as a new Basic Task:
- When Computer Starts
- Add `%USERPROFILE%\run_wsl2_at_startup.vbs` as the program/script to execute.
- Select "Open the Properties Dialog..." on finish.

Additional Task Scheduler Settings:
- Triggers > At Startup > Delay Task for > 30s
- General > Run Whether User Is Logged On or Not
- General > Run With Highest Privileges
- Settings > Uncheck "Stop Task if it Runs Longer Than

(Computer will require restart to finish configuration.)
