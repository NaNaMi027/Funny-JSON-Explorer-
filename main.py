import json
from builder import Builder
from factory import Factory
from star_icon_family import StarIconFamily
from chess_icon_family import ChessIconFamily

# 从文件中读取JSON数据
def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # 读取JSON数据
    json_file_path = 'data.json'
    data = load_data_from_file(json_file_path)
    # 创建tree工厂
    factory = Factory.get_factory("tree")
    # 创建节点树并展示
    builder = Builder(factory)
    root = builder.build(data)
    # 图标族1
    icon_family = StarIconFamily() 
    root.display(icon_family = icon_family)

    # 创建rectangle工厂
    factory = Factory.get_factory("rectangle")
    builder = Builder(factory)
    root = builder.build(data)
    root.display(icon_family = icon_family)

    # 创建tree工厂
    factory = Factory.get_factory("tree")
    # 创建节点树并展示
    builder = Builder(factory)
    root = builder.build(data)
    # 图标族2
    icon_family = ChessIconFamily() 
    root.display(icon_family = icon_family)

    # 创建rectangle工厂
    factory = Factory.get_factory("rectangle")
    builder = Builder(factory)
    root = builder.build(data)
    root.display(icon_family = icon_family)

if __name__ == "__main__":
    main()
