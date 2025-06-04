#include "esphome/core/log.h"
#include "uart_demo.h"

namespace esphome {
namespace uart_demo {

static const char *TAG = "uart_demo.component";

void UARTDemo::setup() {

}

void UARTDemo::loop() {
  while (this->available()) {
    uint8_t c;
    this->read_byte(&c);
    this->handle_char_(c);
  }
}

void UARTDemo::handle_char_(uint8_t c) {
  if (c == '\r')
    return;
  if (c == '\n') {
    std::string s(this->rx_message_.begin(), this->rx_message_.end());
    // if (this->the_text_ != nullptr)
    //   this->the_text_->publish_state(s);
    // if (this->the_sensor_ != nullptr)
    //   this->the_sensor_->publish_state(parse_number<float>(s).value_or(0));
    // if (this->the_binsensor_ != nullptr)
    //   this->the_binsensor_->publish_state(s == "ON");
    this->rx_message_.clear();
    return;
  }
  this->rx_message_.push_back(c);
}

void UARTDemo::dump_config(){
  ESP_LOGCONFIG(TAG, "UART Demo Component");
  // LOG_TEXT_SENSOR("", "The Text Sensor", this->the_text_);
  // LOG_SENSOR("", "The Sensor", this->the_sensor_);
}

void UARTDemo::set_the_switch_1(bool enable) {
  ESP_LOGCONFIG(TAG, "The Switch 1 is %d", enable);
}

void UARTDemo::set_the_switch_2(bool enable) {
  ESP_LOGCONFIG(TAG, "The Switch 2 is %d", enable);
}

void UARTDemo::set_the_button_1() {
  ESP_LOGCONFIG(TAG, "The Button 1 Pressed");
}

void UARTDemo::set_the_button_2() {
  ESP_LOGCONFIG(TAG, "The Button 2 Pressed");
}

void UARTDemo::write_binary(bool state) {
  this->write_str(ONOFF(state));
}

void UARTDemo::ping() {
  this->write_str("PING");
}

void UARTDemo::write_float(float state) {
  this->write_str(to_string(state).c_str());
}

}  // namespace uart_demo
}  // namespace esphome