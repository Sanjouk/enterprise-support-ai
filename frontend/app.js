const statusText = document.getElementById("statusText");
const healthPayload = document.getElementById("healthPayload");
const requestPreview = document.getElementById("requestPreview");
const responsePreview = document.getElementById("responsePreview");
const healthBtn = document.getElementById("healthBtn");
const analyzeBtn = document.getElementById("analyzeBtn");
const ticketInput = document.getElementById("ticketInput");
const customerInput = document.getElementById("customerInput");
const messageInput = document.getElementById("messageInput");

function format(value) {
  return JSON.stringify(value, null, 2);
}

function setStatus(text, kind) {
  statusText.textContent = text;
  statusText.classList.remove("ok", "error");
  if (kind) {
    statusText.classList.add(kind);
  }
}

function logRequest(method, path, body) {
  requestPreview.textContent = format({
    method,
    path,
    body,
    time: new Date().toISOString(),
  });
}

function logResponse(status, latencyMs, payload) {
  responsePreview.textContent = format({
    status,
    latency_ms: latencyMs,
    payload,
  });
}

async function fetchJson(path, init) {
  const startedAt = performance.now();
  const response = await fetch(path, init);
  const latencyMs = Math.round(performance.now() - startedAt);

  const contentType = response.headers.get("content-type") || "";
  let payload;
  if (contentType.includes("application/json")) {
    payload = await response.json();
  } else {
    payload = await response.text();
  }

  return { response, payload, latencyMs };
}

async function checkHealth() {
  healthBtn.disabled = true;
  logRequest("GET", "/health", null);

  try {
    const { response, payload, latencyMs } = await fetchJson("/health");
    if (!response.ok) {
      setStatus("API is unavailable", "error");
      healthPayload.textContent = format(payload);
      logResponse(response.status, latencyMs, payload);
      return;
    }

    setStatus(`API is available (${latencyMs} ms)`, "ok");
    healthPayload.textContent = format(payload);
    logResponse(response.status, latencyMs, payload);
  } catch (error) {
    setStatus("Connection error", "error");
    const payload = { error: error.message };
    healthPayload.textContent = format(payload);
    logResponse(0, 0, payload);
  } finally {
    healthBtn.disabled = false;
  }
}

async function sendTicketAnalyzeRequest() {
  const message = messageInput.value.trim();
  if (!message) {
    messageInput.focus();
    return;
  }

  const ticketId = ticketInput.value.trim();
  const customerId = customerInput.value.trim();
  const body = { message };
  if (ticketId) {
    body.ticket_id = ticketId;
  }
  if (customerId) {
    body.customer_id = customerId;
  }

  analyzeBtn.disabled = true;
  logRequest("POST", "/api/v1/tickets/analyze", body);

  try {
    const { response, payload, latencyMs } = await fetchJson("/api/v1/tickets/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (response.status === 404) {
      logResponse(404, latencyMs, { hint: "Endpoint not found.", original_response: payload });
      return;
    }

    logResponse(response.status, latencyMs, payload);
  } catch (error) {
    logResponse(0, 0, { error: error.message });
  } finally {
    analyzeBtn.disabled = false;
  }
}

healthBtn.addEventListener("click", checkHealth);
analyzeBtn.addEventListener("click", sendTicketAnalyzeRequest);
window.addEventListener("load", checkHealth);
