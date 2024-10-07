extends Node2D

var file_path = 'user://settings.cfg'

func listen_pine(pipe_path, stream_peer):
	while true:
		var file = File.new()
		if file.open(pipe_path, file.READ) == OK:
			var data = file.get_as_text()
			printerr(data)
			if data =="y":
				get_tree().change_scene("res://cj/czcj.tscn")
		else:
			break

func run_python(path :Array, sfzt :bool = false, zszd :bool = true):
	var python_interpreter = "python"  # 或者是 "python3"，取决于系统
	var _run_code = OS.execute(python_interpreter, path, sfzt, [], false, zszd)

func is_first():
	var fe = File.new()
	var config = ConfigFile.new()
	
	if not fe.file_exists(file_path):
		config.set_value("", "first_run", true)
		config.save(file_path)
		run_python(['E:/godotgame/10.6_three/jb/first.py'])

	else:
		var cbcg = config.load(file_path)
		if cbcg == OK:
			if config.get_value("", "first_run") == true:
				return
			else:
				run_python(['E:/godotgame/10.6_three/jb/first.py'])
		else:
			printerr('未知错误')

func _ready():
	is_first()

func _on_Button_button_down():
	get_tree().change_scene("res://cj/dj.tscn")
	run_python(["E:/godotgame/10.6_three/jb/main.py"])
	
