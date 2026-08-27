# Sources

Checked 2026-08-23. These sources support the general delivery safeguards synthesized in
`SKILL.md`. They do not prescribe this package's names, numeric thresholds, role model, or one
universal development ceremony.

## Small, coherent scope

- Google's [Small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html)
  recommends self-contained changes that address one issue and explains that smaller changes are
  easier to review, validate, and roll back. It also rejects splitting necessary tests away from the
  behavior they prove. This supports one-outcome increments and keeping required proof with a change.
- The [Principles behind the Agile Manifesto](https://agilemanifesto.org/principles) favors working
  software, frequent delivery, and simplicity measured by work not done. This package applies that
  principle by requiring planning, delegation, and additional gates only when dependencies or risk
  justify them.

## Plans, acceptance, and changing evidence

- NASA's [SWE-013 Software Plans](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans)
  says software plans should identify work, commitments, and risks and remain complete, workable,
  consistent, and verifiable as conditions change. Its scope is aerospace assurance; this package
  borrows plan completeness and revision when facts invalidate an approach, not NASA's assurance
  level.
- NASA's [SWE-034 Acceptance Criteria](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria)
  recommends documented, measurable criteria that give stakeholders a shared basis for readiness.
  This supports defining observable proof before implementation and distinguishing completion from
  a plausible report. Its scope is aerospace assurance, not a universal software process.

## Risk and independent evidence

- NIST [SP 800-218, Secure Software Development Framework 1.1](https://doi.org/10.6028/NIST.SP.800-218)
  organizes secure development around risk-based practices, review or analysis, and retained
  evidence. This package generalizes that principle into named risk triggers; NIST does not prescribe
  the six-row taxonomy in `SKILL.md`.
- Anthropic's engineering report,
  [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system),
  reports that clear objectives, output formats, tool guidance, and task boundaries reduce duplicated
  work and gaps, while multi-agent coordination has substantial overhead and performs poorly on
  highly dependent work. It is a field report about one research system, not a controlled study of
  software teams. This package uses it only to support bounded handoffs and limited parallelism.

## Catalog conclusions

- Engagement mode is selected from dependency, design, and proof boundaries rather than a mandatory
  lifecycle. The source set supports small coherent changes, measurable readiness, explicit risk,
  and bounded handoffs; it does not supply the mode names.
- The six risk triggers are a local operational taxonomy. Their responses synthesize NIST's
  risk-based evidence principle with common compatibility and recovery boundaries.
- GitHub delivery is a separate authority boundary because externally stored mutations have a
  different target, account, and verification contract from local development. This separation is
  a catalog design conclusion, not a claim made by the sources above.
- Repository and material-risk boundaries are treated as verification boundaries, so dependent
  implementation phases remain separate even when they cannot run in parallel. The atomic-outcome
  exception preserves Google's guidance to keep behavior with the proof that establishes it; its
  wording and application are catalog conclusions.
- Implementation and completed-change review require different role fit and evidence. The exact
  finished-change review brief is a catalog conclusion derived from measurable acceptance, retained
  evidence, and the team's separation of implementation from independent judgment.
