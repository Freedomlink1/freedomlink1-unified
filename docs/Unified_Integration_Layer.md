# Freedomlink1 Unified Integration Layer

The Unified Integration Layer defines how the three primary repos and hardware/institutional anchors form one coherent system:

- freedomlink1-protocol
- freedomlink1-governance
- freedomlink1-unified
- Rootstone-I hardware root
- PPTF institutional layer

## 1. Layer Model

**Protocol Layer**
- Smart contracts
- Deployment scripts
- CI/CD
- Dashboards
- Analytics
- Multi-chain manifests

**Governance Layer**
- Epoch lineage
- Seals and Merkle roots
- Sovereign signatures
- Proclamations and doctrines
- Sentinel directives
- Continuity frameworks

**Unified Layer**
- Cross-repo manifests
- Epoch -> contract bindings
- Sovereign -> deployment bindings
- Rootstone-I -> protocol bindings
- PPTF -> protocol bindings
- Multi-chain mapping

## 2. Binding Types

- **Epoch bindings:** `unified/epoch.bindings.json`
- **Sovereign bindings:** `unified/sovereign.bindings.json`
- **Deployment bindings:** `unified/deployment.bindings.json`
- **Hardware bindings:** `unified/rootstone.bindings.json`
- **Institutional bindings:** `unified/pptf.bindings.json`

Each binding file is declarative and versioned via `versioning/`.

## 3. Evolution

New epochs, chains, hardware anchors, or institutional layers are added by:

- extending the relevant `*.bindings.json`
- bumping `unified.version`
- referencing new artifacts in protocol/governance repos

This keeps Freedomlink1 extensible without collapsing into a monolith.
