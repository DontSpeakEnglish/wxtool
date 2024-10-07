# 这是附加到 Label 节点的 GDScript

extends Label

var text_list = ["正在检测窗口...", "正在检测窗口..", "正在检测窗口.", "正在检测窗口", "正在检测窗口.", "正在检测窗口.."] # 要显示的文本列表
var current_text_index = 0 # 当前文本在列表中的索引

func _ready():
	# 在场景准备就绪时，连接 Timer 的 timeout 信号到 Label 的 _on_Timer_timeout 函数
	$Timer.connect("timeout", self, "_on_Timer_timeout")
	$Timer.start() # 启动计时器

func _on_Timer_timeout():
	# 计时器超时时调用，更换 Label 文本
	current_text_index = (current_text_index + 1) % text_list.size() # 更新索引
	text = text_list[current_text_index] # 设置新的文本
