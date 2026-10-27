FROM ubuntu:24.04 AS build
RUN apt-get update && apt-get install -y git build-essential cmake libssl-dev
ENV CMAKE_POLICY_VERSION_MINIMUM=3.5
RUN git clone https://github.com/eclipse/paho.mqtt-sn.embedded-c.git /src
WORKDIR /src/MQTTSNGateway
RUN ./build.sh udp
RUN mkdir -p /opt/gw && \
    cp "$(find /src -name MQTT-SNGateway -type f | head -1)" /opt/gw/ && \
    cp clients.conf predefinedTopic.conf /opt/gw/ && \
    find /src -name 'libMQTTSNPacket.so*' -exec cp -a {} /opt/gw/ \;

FROM ubuntu:24.04
RUN apt-get update && apt-get install -y libssl3 && rm -rf /var/lib/apt/lists/*
COPY --from=build /opt/gw /opt/gw
ENV LD_LIBRARY_PATH=/opt/gw
WORKDIR /opt/gw
RUN ldd ./MQTT-SNGateway
CMD ["./MQTT-SNGateway", "-f", "gateway.conf"]
