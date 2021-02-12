package main

import "fmt"

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for index, v := range nums {
		m[v] = index
	}
	for index, v := range nums {
		_, ok := m[target - v]
		if ok && index != m[target - v] {
			return []int{index, m[target - v]}
		}
	}
	return nil
}

func main() {
	nums := []int{2, 3, 4}
	target := 6
	result := twoSum(nums, target)
	for _, v := range result {
		fmt.Println(v)
	}
}

