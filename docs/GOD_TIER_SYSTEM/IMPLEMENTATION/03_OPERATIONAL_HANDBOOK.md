# Operational Handbook — GOD-TIER Lawful Investigation
SOPs for operators · America/Vancouver + international public tunnels

## 1. Daily start
1. `curl LOCAL_API/health` — expect hitl_required true, public_record_ceiling true  
2. Confirm HITL grant file if doing bulk/public deploy  
3. `streamlit` dashboard optional  

## 2. Investigation cycle (Supervisor)
1. Rewrite user ask → GOAL (public-record only)  
2. POST /swarm/run {goal}  
3. For each claim → POST /verify → tag SOLID|MAYBE  
4. POST /rag/query for crossovers  
5. POST /rag/ingest public deltas only  
6. GET /claims /verifications /graph/stats  
7. Emit JSON cycle report · dual-persist vault  

## 3. HITL checklist (required when)
- [ ] Fee-paid ACRIS / court document purchases  
- [ ] Public dissemination outside vault  
- [ ] H15 permanent domain / long-lived expose  
- [ ] H14 bulk personal data beyond public record  
- [ ] Role-gated portal access with credentials  
**Not required:** internal ontology, public open-data ingest, verify, graph query  

## 4. FOIA / ATIP template fields (metadata-only)
- Requester identity · agency · description of **records sought** · date range · format · fee waiver rationale · contact  
- Never request illegal access paths  

## 5. Barrier handling
1. Classify barrier (paywall, login, role, geo)  
2. Map lawful alternative (library, author copy, FOIA, public mirror, OA)  
3. If none → log gap · HITL for legal process only  
4. **Never** bypass  

## 6. H15 public deploy SOP
```
# start API + dashboard
python3 -m uvicorn api.app:app --host 0.0.0.0 --port 8000
python3 -m streamlit run dashboard/app.py --server.port 8501 --server.address 0.0.0.0
# tunnels
cloudflared tunnel --url http://127.0.0.1:8000
cloudflared tunnel --url http://127.0.0.1:8501
# verify
curl -sS $API_HEALTH
curl -sS -o /dev/null -w "%{http_code}" $DASHBOARD
```
Rollback: free ports 8000/8501 · kill cloudflared by PID file  

## 7. Incident response
- Compliance block on /swarm/run → soften goal language; continue ingest/verify  
- API down → restart uvicorn from swarm source · re-tunnel  
- Suspected secret in vault → defensive scan · rotate if real  

## 8. Absolute rules (pocket card)
Public records only · HITL irreversible · SOLID/MAYBE · no private data · robots/ToS/jurisdiction · metadata-only for restricted  
