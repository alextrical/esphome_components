#include "uart_example.h"
#include "esphome/core/log.h"

namespace esphome {
namespace uart_example {

static const char *const TAG = "uart_example";

void UARTExampleSensor::setup() {
  ESP_LOGD(TAG, "Setting up UARTExample sensor");
  // Initialize parent UART component
//   this->set_baud_rate(9600);  // Default baud rate, override in YAML
}

void UARTExampleSensor::loop() {
    while (this->available()) {
        uint8_t c;
        this->read_byte(&c);
        this->handle_char_(c);
    }
    if (this->temperature_sensor_ != nullptr)
        ESP_LOGCONFIG(TAG, "UARTExample Sensor: %s", "30");
        this->temperature_sensor_->publish_state(30);
    if (this->humidity_sensor_ != nullptr)
        this->humidity_sensor_->publish_state(parse_number<float>("16.83").value_or(0));
}

void UARTExampleSensor::handle_char_(uint8_t c) {
  if (c == '\r')
    return;
  if (c == '\n') {
    std::string s(this->rx_message_.begin(), this->rx_message_.end());
    if (this->temperature_sensor_ != nullptr)
      this->temperature_sensor_->publish_state(parse_number<float>(s).value_or(0));
    if (this->humidity_sensor_ != nullptr)
      this->humidity_sensor_->publish_state(parse_number<float>(s).value_or(0));
    this->rx_message_.clear();
    return;
  }
  this->rx_message_.push_back(c);
}

void UARTExampleSensor::dump_config() {
  ESP_LOGCONFIG(TAG, "UARTExample Sensor:");
  LOG_SENSOR("  ", "Temperature", this->temperature_sensor_);
  LOG_SENSOR("  ", "Humidity", this->humidity_sensor_);
}

}  // namespace uart_example
}  // namespace esphome
