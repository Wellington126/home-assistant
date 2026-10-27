#!/bin/bash
sleep 5
while true; do
  T=$((20 + RANDOM % 10))
  if mqtt-sn-pub -h gateway-sn -p 10000 -t casa/sala/temperatura -m "$T"; then
    echo "publicado: $T"
  else
    echo "falha ao publicar: $T"
  fi
  sleep 5
done
