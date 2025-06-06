#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
namespace uart_example {

class UARTExampleSensor : public Component, public uart::UARTDevice {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;

  void set_temperature_sensor(sensor::Sensor *temp_sensor) {
    temperature_sensor_ = temp_sensor;
  }

  void set_humidity_sensor(sensor::Sensor *humidity_sensor) {
    humidity_sensor_ = humidity_sensor;
  }

 protected:
  sensor::Sensor *temperature_sensor_{nullptr};
  sensor::Sensor *humidity_sensor_{nullptr};
  void handle_char_(uint8_t c);
  std::vector<uint8_t> rx_message_;
};

}  // namespace uart_example
}  // namespace esphome
