FIXTURES = {
 "hidden_constraint": {"target":"T_CURRENT","hidden_constraint":False,"repaired":False,"expected_cut":"REPRESENTATION"},
 "wrong_object": {"target":"T_OLD","authoritative_target":"T_CURRENT","hidden_constraint":True,"repaired":False,"expected_cut":"OBJECT_IDENTITY"},
 "authority_conflict": {"target":"T_CURRENT","hidden_constraint":True,"repaired":False,"authority_denied":True,"expected_cut":"AUTHORITY"},
 "binding_failure": {"target":"T_CURRENT","hidden_constraint":True,"repaired":False,"worker_available":False,"expected_cut":"BINDING"},
 "incomparable": {"target":"T_CURRENT","hidden_constraint":True,"repaired":False,"alternatives":["A","B"],"relation":"INCOMPARABLE","expected_cut":"ROUTING_UNCERTAINTY"},
 "no_gain": {"target":"T_CURRENT","hidden_constraint":True,"repaired":True,"expected_cut":"NO_GAIN"}
}
