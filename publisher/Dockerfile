FROM ubuntu:24.04
RUN apt-get update && apt-get install -y git build-essential
RUN git clone https://github.com/njh/mqtt-sn-tools.git /src && cd /src && \
    git checkout a1dd870 && \
    sed -i 's/memcpy(packet.data, data, sizeof(packet.data));/memcpy(packet.data, data, data_len);/' mqtt-sn.c && \
    grep -n 'memcpy(packet.data, data, data_len)' mqtt-sn.c && \
    make && make install
COPY publish.sh /publish.sh
RUN chmod +x /publish.sh
CMD ["/publish.sh"]
