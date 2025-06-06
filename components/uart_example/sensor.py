import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import CONF_ID, CONF_TEMPERATURE, CONF_HUMIDITY

DEPENDENCIES = ['uart']

uart_example_ns = cg.esphome_ns.namespace('uart_example')
UARTExampleSensor = uart_example_ns.class_('UARTExampleSensor', 
                                         cg.Component, 
                                         uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({
  cv.GenerateID(): cv.declare_id(UARTExampleSensor),
  cv.Required(CONF_TEMPERATURE): sensor.sensor_schema(
    unit_of_measurement="°C",
    accuracy_decimals=1
  ),
  cv.Required(CONF_HUMIDITY): sensor.sensor_schema(
    unit_of_measurement="%",
    accuracy_decimals=1
  ),
}).extend(uart.UART_DEVICE_SCHEMA)

def to_code(config):
  var = cg.new_Pvariable(config[CONF_ID])
  yield uart.register_uart_device(var, config)
  
  if CONF_TEMPERATURE in config:
    sens = yield sensor.new_sensor(config[CONF_TEMPERATURE])
    cg.add(var.set_temperature_sensor(sens))
    
  if CONF_HUMIDITY in config:
    sens = yield sensor.new_sensor(config[CONF_HUMIDITY])
    cg.add(var.set_humidity_sensor(sens))
