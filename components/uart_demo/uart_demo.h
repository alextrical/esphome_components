#pragma once

#include "esphome/core/component.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
namespace uart_demo {

class UARTDemo : public Component,  public uart::UARTDevice {
 public:
  float get_setup_priority() const override { return setup_priority::LATE; }
  void setup() override;
  void loop() override;
  void dump_config() override;

  void set_the_text(text_sensor::TextSensor *text_sensor) { the_text_ = text_sensor; }
  void set_the_sensor(sensor::Sensor *sensor) { the_sensor_ = sensor; }
  void set_the_binsensor(binary_sensor::BinarySensor *sensor) { the_binsensor_ = sensor; }

  void write_binary(bool value);
  void write_float(float value);
  void ping();
 protected:
  text_sensor::TextSensor *the_text_{nullptr};
  sensor::Sensor *the_sensor_{nullptr};
  binary_sensor::BinarySensor *the_binsensor_{nullptr};

  void handle_char_(uint8_t c);
  std::vector<uint8_t> rx_message_;
};

}  // namespace uart_demo
}  // namespace esphome
