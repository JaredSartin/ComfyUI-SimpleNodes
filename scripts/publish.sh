#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <package-file>"
  exit 2
fi

PACKAGE_FILE="$1"
: "${COMFY_REGISTRY_TOKEN:?Need to set COMFY_REGISTRY_TOKEN as a repo secret. See README.md}" 
REGISTRY_URL="${COMFY_REGISTRY_URL:-https://docs.comfy.org/registry/publishing}"

echo "Publishing ${PACKAGE_FILE} to ${REGISTRY_URL}"

# The exact upload API and parameters are defined by the ComfyUI registry.
# The registry docs: https://docs.comfy.org/registry/publishing
# Example placeholder curl call (update to the actual endpoint/parameters):

curl -v -X POST \
  -H "Authorization: Bearer ${COMFY_REGISTRY_TOKEN}" \
  -F "package=@${PACKAGE_FILE}" \
  "${REGISTRY_URL}"

echo "Upload step finished (check response above). If the registry API requires different fields or a different endpoint, update scripts/publish.sh accordingly."
