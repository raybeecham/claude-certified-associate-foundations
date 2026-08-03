# Lesson 7A: Module 6 Quiz

## Result

```text
Full marks — 5 of 5
```

This original public-safe quiz assesses governance judgment across five areas:

1. use-case appropriateness;
2. Skill and feature trust;
3. data sensitivity and persistence controls;
4. policy-to-practice Diligence; and
5. ethical bias and fairness review.

The questions below are not copied from a live certification exam. They are original study scenarios based on the concepts taught in Module 6.

---

# Question 1: Consequential final decisions

A public-assistance office proposes using an AI system to issue final, unreviewed eligibility decisions. Applicants may lose access to essential services based on the output.

Which classification is most appropriate?

A. Fully appropriate because automation improves consistency  
B. Appropriate with occasional quality sampling  
C. Inappropriate for AI ownership because the consequence is significant and accountability must remain with an authorized human decision-maker  
D. Appropriate if the strongest available model is selected

## Correct answer

**C — Inappropriate for AI ownership.**

The load-bearing criteria are consequence of error and non-transferable accountability. A stronger model does not accept legal, professional, or organizational responsibility. An authorized human must make and own the final decision, with evidence, review criteria, and recourse for affected people.

```text
High consequence
+ difficult-to-reverse effect
+ non-transferable accountability
→ retain human ownership
```

---

# Question 2: Unvetted executable capability

A teammate sends you a third-party Skill called `MeetingNotePolisher`. The publisher is unknown. The package contains scripts and references to file and connector tools, but there is no evidence of organizational review.

What is the responsible next step?

A. Enable it because the teammate has used it successfully  
B. Enable it in a normal work session and observe its behavior  
C. Inspect the source, bundle, dependencies, and effective reach; do not enable it on organizational data until the appropriate review authority approves it  
D. Assume its access is limited to meeting notes because of its name

## Correct answer

**C — Inspect and escalate before enabling.**

A recommendation is not provenance, a product name is not a permission boundary, and useful output does not prove safe behavior. The Skill's effective reach depends on what the real session can access, execute, persist, or change.

```text
Unknown source
+ executable bundle
+ unclear effective reach
→ inspect and escalate
```

---

# Question 3: Confidential data and persistence

A user needs to analyze a confidential internal document. Organizational policy allows the document in the approved Claude workspace, but the conversation should not enter ordinary chat history or Memory.

Which option best fits?

A. Use a standard chat with Memory enabled  
B. Use Incognito in the approved workspace, while recognizing that organizational retention and export rules may still apply  
C. Upload the file to a broadly shared Project  
D. Use a stronger model because model selection controls persistence

## Correct answer

**B — Use Incognito inside the approved processing boundary.**

Processing authorization comes first. Incognito can reduce ordinary history and Memory persistence, but it does not override organizational retention, export, legal, contractual, or data-handling rules.

```text
Approved to process
+ persistence should be reduced
→ Incognito may fit
```

```text
Incognito
≠
permission to process prohibited data
```

---

# Question 4: Policy-to-practice drift

A monthly audit finds that several employees use personal AI accounts for draft customer deliverables because the approved workspace requires several extra login steps.

What is the strongest governance response?

A. Accept the workaround because it improves productivity  
B. Treat it only as individual misconduct  
C. Record a Diligence gap, contain the unapproved use, and repair the workflow so the compliant route becomes the practical default  
D. Prohibit all AI use by the team

## Correct answer

**C — Record, contain, repair, and verify.**

The observed behavior conflicts with policy, but the inconvenient approved path is also a root cause. Durable remediation should address the workflow, access, communication, and technical controls rather than relying only on reminders or punishment.

```text
Policy requirement
≠
Observed practice
→ Diligence gap
```

Closure requires evidence that the corrected path is being used.

---

# Question 5: Hidden exclusion risk

A recruiting workflow uses AI to remove applicants before the hiring manager sees them. The manager interviews only the remaining candidates, and no qualified person reviews the excluded group.

Which ethical concern is most directly raised?

A. Copyright ownership of résumé text  
B. Systematic bias or unfair exclusion that remains invisible because the filtered-out cases receive no human review  
C. The model has accepted accountability for the hiring decision  
D. The only issue is whether applicants were told AI was used

## Correct answer

**B — Bias and unfair exclusion.**

Disclosure may also matter, but the defining risk is that the system can systematically disadvantage applicants while the accountable human never sees the exclusions. Accountability remains with the employer and its authorized decision-makers; it does not transfer to the model.

A responsible design requires:

- review of selection criteria and proxy variables;
- representative and edge-case testing;
- qualified human review of exclusions;
- evidence and consistency checks;
- explanation and correction paths where required; and
- monitoring for unequal outcomes.

---

# Competency map

| Question | Primary competency | Key distinction |
|---|---|---|
| 1 | Use-case classification | Capability does not transfer accountability |
| 2 | Skill trust | Recommendation and name do not establish provenance or safe reach |
| 3 | Data controls | Processing authorization and persistence are separate decisions |
| 4 | Organizational Diligence | Gaps require root-cause repair and verified closure |
| 5 | Ethical implications | Accurate-looking automation can hide systematic unfairness |

---

# Quiz shortcut

```text
Final consequential determination
→ retain authorized human ownership

Unknown executable Skill
→ inspect source, bundle, and effective reach

Confidential approved data with no ordinary persistence
→ Incognito may fit, subject to organizational retention

Policy and actual use diverge
→ record and close a Diligence gap

Automated exclusions receive no human review
→ bias and fairness risk
```

---

# Common distractors

## Stronger-model substitution

A stronger model does not repair:

- inappropriate delegation;
- missing accountability;
- unapproved data processing;
- excessive permissions;
- absent human review;
- policy violations; or
- unfair workflow design.

## Convenience-first reasoning

Productivity does not automatically justify bypassing:

- approved entry points;
- data classification;
- Skill review;
- human gates; or
- ethical safeguards.

## Human-in-the-loop labels

A meaningful gate requires:

- a qualified role;
- evidence access;
- specific review criteria;
- timing before consequence;
- authority to modify or reject; and
- escalation and recourse.

## Accountability transfer

```text
AI influenced the result
      ≠
AI owns the result
```

The responsible human and organization remain accountable.

---

# Retention questions

Confirm that you can explain:

1. why a high-consequence final determination should remain human-owned;
2. why a Skill's name and recommendation do not establish trust;
3. why Incognito is not permission to process Red data;
4. why policy friction can create a systemic Diligence gap; and
5. why unreviewed exclusions create a distinct fairness risk.

---

# Short recap

```text
1. Classify the use before selecting the model.
2. Treat Skills as software-like capabilities.
3. Classify data before choosing persistence controls.
4. Compare real behavior with current policy.
5. Review ordinary outputs for bias and unfair effects.
6. Preserve accountable human authority and recourse.
```

## Educational-use notice

This quiz is an original educational exercise. It does not reproduce proprietary certification questions and does not constitute legal, privacy, security, compliance, employment, public-benefits, or other professional advice.
