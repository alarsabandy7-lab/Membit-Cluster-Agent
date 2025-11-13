# Context Agent — Membit Intelligence Bot (V64 Sandbox Build)

import logging
from cluster_agent_v61 import client

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    logging.info("===============================================================")
    logging.info("🚀 Launching Context Agent V64 — Membit Intelligence Sandbox")
    logging.info("===============================================================")
    try:
        client.run()
    except KeyboardInterrupt:
        logging.info("🛑 Gracefully shutting down Context Agent V64.")
