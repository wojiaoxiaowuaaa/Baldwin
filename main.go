package main

import (
	"fmt"
	"log"
	"os/exec"
)

func main() {
	// 定义Python脚本路径和参数
	pythonScript := "delete_dir.py"
	arg := "111"
	// 创建命令
	cmd := exec.Command("python3", pythonScript, arg)

	// 获取输出
	output, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatalf("执行Python脚本失败: %v\n输出: %s", err, output)
	}

	// 打印输出
	fmt.Printf("Python脚本输出:\n%s\n", output)
}