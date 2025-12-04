#!/usr/bin/env python3
"""
Windows 任务计划程序设置脚本
用于自动配置每日运行任务
"""

import os
import sys
from pathlib import Path

def create_task_scheduler_xml():
    """生成任务计划程序的 XML 配置文件"""
    
    script_dir = Path(__file__).parent.absolute()
    python_exe = sys.executable
    script_path = script_dir / "arxiv_fetcher.py"
    
    xml_content = f"""<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2024-01-01T00:00:00</Date>
    <Author>arXiv Paper Fetcher</Author>
    <Description>每日自动从 arXiv 获取相关论文</Description>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>2024-01-01T02:00:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-18</UserId>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>false</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT1H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>"{python_exe}"</Command>
      <Arguments>"{script_path}"</Arguments>
      <WorkingDirectory>"{script_dir}"</WorkingDirectory>
    </Exec>
  </Actions>
</Task>"""
    
    xml_file = script_dir / "arxiv_daily_task.xml"
    with open(xml_file, 'w', encoding='utf-16') as f:
        f.write(xml_content)
    
    print(f"已生成任务计划程序配置文件: {xml_file}")
    print("\n使用方法:")
    print(f"1. 以管理员身份打开 PowerShell")
    print(f"2. 运行以下命令:")
    print(f'   schtasks /Create /TN "arXiv Paper Fetcher" /XML "{xml_file}" /F')
    print("\n或者手动操作:")
    print("1. 打开'任务计划程序'")
    print("2. 点击'导入任务'")
    print(f"3. 选择文件: {xml_file}")

if __name__ == "__main__":
    create_task_scheduler_xml()


