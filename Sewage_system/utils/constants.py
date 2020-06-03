
# 登陆后存储在session中的ID
LOGIN_SESSION_ID = 'user_id'
LOGIN_SENDOR_ID = 'SENDOR_id'


# 工作人员级别
LEVEL_ORDINARY = 1
LEVEL_ADMIN = 1
LEVEL_CHOICES = (
        (1, '普通员工'),
        (2, '主管')
    )

# 处理池号
CELL_ID_ONE_1 = 1-1

CELL_ID_ONE_2 = 1-2     # 主要分离固体

CELL_ID_ONE_3 = 1-3
CELL_ID_TWO_1 = 2-1

CELL_ID_TWO_2 = 2-2     # 主要吸收重金属
CELL_ID_TWO_3 = 2-3     # 重金属吸收后产生的固体

CELL_ID_THREE_1 = 3-1   # 吸收氨氮

CELL_ID_THREE_2 = 3-2

CELL_ID_CHOICES = (
    (CELL_ID_ONE_1, '初次沉淀池'),
    (CELL_ID_ONE_2, '1号过滤池'),
    (CELL_ID_ONE_2, '二次沉淀池'),
    (CELL_ID_TWO_1, '2号沉淀池'),
    (CELL_ID_TWO_2, '重金属吸收池'),
    (CELL_ID_TWO_3, '2号过滤池'),
    (CELL_ID_THREE_1, '氨氮吸收池'),
    (CELL_ID_THREE_2, '氨氮吸收池'),
)

# 处理的元素种类
TYPE_SOLID = 's'
TYPE_METAL = 'm'
TYPE_PH = 'p'
TYPE_AN = 'a'
TYPE_CHOICES = (
    (TYPE_SOLID, '固体含量'),
    (TYPE_METAL, '重金属含量'),
    (TYPE_PH, 'PH值'),
    (TYPE_AN, '氨氮含量')
)

# 设备状态选择
EQUIPMENT_STATUS_NORMAL = 1
EQUIPMENT_STATUS_REPAIR = 2
EQUIPMENT_STATUS_ADD = 3

EQUIPMENT_STATUS_CHOICES = (
    (EQUIPMENT_STATUS_NORMAL, '正常状态'),
    (EQUIPMENT_STATUS_REPAIR, '维修状态'),
    (EQUIPMENT_STATUS_ADD, '添加药物'),
)

# PH不在范围
ALERT_STATUS_PH_HIGH = 2
ALERT_STATUS_PH_LOW = -1
ALERT_STATUS_PH_CHOICES = (
    (ALERT_STATUS_PH_HIGH, 'PH偏高'),
    (ALERT_STATUS_PH_LOW, 'PH偏低'),
)

# 处理不达标报警类型
ALERT_STATUS_SOLID = 0
ALERT_STATUS_METAL = 0
ALERT_STATUS_AN = 0
ALERT_STATUS_CHOICES = (
    (ALERT_STATUS_SOLID, '固体处理不达标'),
    (ALERT_STATUS_METAL, '重金属处理不达标'),
    (ALERT_STATUS_AN, '氨氮处理不达标'),
)

# 设备报警类型
EQUIP_ALERT_STATUS_REPAIR = 1
EQUIP_ALERT_STATUS_ADD = 2
EQUIP_ALERT_STATUS_CHOICES =(
    (EQUIP_ALERT_STATUS_REPAIR, '设备维修'),
    (EQUIP_ALERT_STATUS_ADD, '药物不足'),
    )

# 固体传感器号
SENSOR_SOLID_ONE = 's-1'
SENSOR_SOLID_TOW = 's-2'
SENSOR_SOLID_FOUR = 's-3'
SENSOR_SOLID_CHOICES = (
    (SENSOR_SOLID_ONE, '固体检测传感器一号'),
    (SENSOR_SOLID_TOW, '固体检测传感器二号'),
    (SENSOR_SOLID_FOUR, '固体检测传感器三号'),
    )

# PH传感器号
SENSOR_PH_ONE = 'ph-1-1'
SENSOR_PH_TOW = 'ph-1-2'  # 数据要多
SENSOR_PH_THREE = 'ph-1-3'

SENSOR_PH_FOUR = 'ph-2-1'
SENSOR_PH_FIVE = 'ph-2-2'     # 数据要多
SENSOR_PH_SIX = 'ph-2-3'

SENSOR_PH_SEVEN = 'ph-2-4'

SENSOR_PH_EIGHT = 'ph-3-1'
SENSOR_PH_NINE = 'ph-3-2'      # 数据要多
SENSOR_PH_TEN = 'ph-3-3'

SENSOR_PH_CHOICES = (
    (SENSOR_PH_ONE, 'PH检测传感器一号'),
    (SENSOR_PH_TOW, 'PH检测传感器二号'),
    (SENSOR_PH_THREE, 'PH检测传感器三号'),
    (SENSOR_PH_FOUR, 'PH检测传感器四号'),
    (SENSOR_PH_FIVE, 'PH检测传感器五号'),
    (SENSOR_PH_SIX, 'PH检测传感器六号'),
    (SENSOR_PH_SEVEN, 'PH检测传感器七号'),
    (SENSOR_PH_EIGHT, 'PH检测传感器八号'),
    (SENSOR_PH_NINE, 'PH检测传感器九号'),
    (SENSOR_PH_TEN, 'PH检测传感器十号')
    ,)

SENSOR_METAL_ONE = 'm-1'
SENSOR_METAL_TOW = 'm-2'
SENSOR_AN_ONE = 'a-1'
SENSOR_AN_TOW = 'a-2'
SENSOR_METAL_CHOICES = (
    (SENSOR_METAL_ONE, '重金属检测传感器一号'),
    (SENSOR_METAL_TOW, '重金属检测传感器二号'),)
SENSOR_AN_CHOICES = (
    (SENSOR_AN_ONE, '氨氮检测传感器一号'),
    (SENSOR_AN_TOW, '氨氮检测传感器二号'),
)

# 控制器设备
CONTROL_PH_ONE = 'c-ph-1'
CONTROL_PH_TOW = 'c-ph-2'
CONTROL_PH_THREE = 'c-ph-3'
CONTROL_PH_FOUR = 'c-ph-4'

CONTROL_SOLID_ONE = 'c-s-1'
CONTROL_SOLID_TOW = 'c-s-2'

CONTROL_METAL_ONE = 'c-m'
CONTROL_AN_ONE = 'c-a'

# 设备选择
EQUIP_CHOICES = (
    (SENSOR_SOLID_ONE, '固体检测传感器一号'),
    (SENSOR_SOLID_TOW, '固体检测传感器二号'),
    (SENSOR_SOLID_FOUR, '固体检测传感器三号'),

    (SENSOR_PH_ONE, 'PH检测传感器一号'),
    (SENSOR_PH_TOW, 'PH检测传感器二号'),
    (SENSOR_PH_THREE, 'PH检测传感器三号'),
    (SENSOR_PH_FOUR, 'PH检测传感器四号'),
    (SENSOR_PH_FIVE, 'PH检测传感器五号'),
    (SENSOR_PH_SIX, 'PH检测传感器六号'),
    (SENSOR_PH_SEVEN, 'PH检测传感器七号'),
    (SENSOR_PH_EIGHT, 'PH检测传感器八号'),
    (SENSOR_PH_NINE, 'PH检测传感器九号'),
    (SENSOR_PH_TEN, 'PH检测传感器十号'),

    (SENSOR_METAL_ONE, '重金属检测传感器一号'),
    (SENSOR_METAL_TOW, '重金属检测传感器二号'),

    (SENSOR_AN_ONE, '氨氮检测传感器一号'),
    (SENSOR_AN_TOW, '氨氮检测传感器二号'),

    (CONTROL_PH_ONE, 'PH调节控制器1'),
    (CONTROL_PH_TOW, 'PH调节控制器2'),
    (CONTROL_PH_THREE, 'PH调节控制器3'),
    (CONTROL_PH_FOUR, 'PH调节控制器4'),

    (CONTROL_SOLID_ONE, '固液分离控制器1'),
    (CONTROL_SOLID_TOW, '固液分离控制器2'),

    (CONTROL_METAL_ONE, '重金属调节控制器'),

    (CONTROL_AN_ONE, '氨氮调节控制器'),
)
