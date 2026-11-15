import express from "express";
import mongoose from "mongoose";
import { getOnlineUsersCount } from "../lib/socket.js";

const router = express.Router();

let requestCount = 0;
const startTime = Date.now();

// Middleware to count requests
export function metricsCollectorMiddleware(req, res, next) {
  requestCount++;
  next();
}

router.get("/", (req, res) => {
  const dbConnected = mongoose.connection.readyState === 1 ? 1 : 0;
  const memoryUsage = process.memoryUsage();
  const uptimeSeconds = Math.floor((Date.now() - startTime) / 1000);
  const activeSockets = getOnlineUsersCount();

  const metrics = [
    "# HELP chat_active_socket_connections Number of active real-time WebSocket clients",
    "# TYPE chat_active_socket_connections gauge",
    `chat_active_socket_connections ${activeSockets}`,
    "",
    "# HELP chat_http_requests_total Total number of HTTP requests received",
    "# TYPE chat_http_requests_total counter",
    `chat_http_requests_total ${requestCount}`,
    "",
    "# HELP chat_database_connected MongoDB connection readiness status (1=connected, 0=disconnected)",
    "# TYPE chat_database_connected gauge",
    `chat_database_connected ${dbConnected}`,
    "",
    "# HELP nodejs_process_uptime_seconds Application uptime in seconds",
    "# TYPE nodejs_process_uptime_seconds gauge",
    `nodejs_process_uptime_seconds ${uptimeSeconds}`,
    "",
    "# HELP nodejs_heap_used_bytes Memory heap currently allocated in bytes",
    "# TYPE nodejs_heap_used_bytes gauge",
    `nodejs_heap_used_bytes ${memoryUsage.heapUsed}`,
    "",
    "# HELP nodejs_heap_total_bytes Total memory heap allocated in bytes",
    "# TYPE nodejs_heap_total_bytes gauge",
    `nodejs_heap_total_bytes ${memoryUsage.heapTotal}`,
    "",
    "# HELP nodejs_rss_bytes Resident set size in bytes",
    "# TYPE nodejs_rss_bytes gauge",
    `nodejs_rss_bytes ${memoryUsage.rss}`,
    ""
  ].join("\n");

  res.setHeader("Content-Type", "text/plain; version=0.0.4; charset=utf-8");
  res.send(metrics);
});

export default router;
