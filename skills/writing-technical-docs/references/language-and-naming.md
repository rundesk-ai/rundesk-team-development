# Write it so it survives being read

Accurate documentation still fails when the reader cannot scan it, or when the words drift from the
words the software uses. These rules are about the prose itself. They cost nothing at writing time
and are expensive to retrofit.

## Use the software's own words

The term the interface uses is the term the page uses. A parameter named `attempts` is `attempts`
everywhere on the page — never "tries", "retries", or "the count" in the sentence next to it.

Google's field-naming guidance states the cost directly: using the same name for different things,
or different names for the same thing, baffles the reader, and readers rarely use one API in
isolation. Documentation multiplies that effect, because a reader who meets a synonym assumes a
distinction exists and goes looking for it.

Before drafting, list the terms the page will use and their source in the code. Then hold the list:

```text
Term        Source in the software           Never write instead
attempts    retry(fn, attempts=...)          tries, retries, count, max
backoff     retry(fn, backoff=...)           delay, wait, sleep interval
propagates  behavior of a non-retried error  bubbles up, escapes, throws out
```

**When the software's name is poor, document the name that exists.** A page is not a rename. Record
the mismatch as a note or an issue; do not quietly improve the identifier in prose, or the reader
searching the codebase for your word finds nothing.

Define a term once, at first use, and never redefine it later in the same page. If two parts of the
system genuinely use one word for two things, say so explicitly rather than letting context carry it.

## One verb per meaning

Pick one verb for each action and hold it across the page:

| Meaning | Choose one | Do not mix in |
|---|---|---|
| An error leaves a function | `raises` | throws, emits, returns an error |
| An error passes through unhandled | `propagates` | bubbles, escapes, falls through |
| A function is executed | `calls` | invokes, runs, triggers, executes |
| A value comes back | `returns` | gives back, yields, produces |
| Work is repeated after failure | `retries` | re-attempts, tries again, repeats |

A synonym reads as a deliberate distinction. In reference documentation that is a false signal, and
the reader pays for it by looking for a difference that is not there.

## Name the meaning in a label; ask the reader's question in a heading

**Table columns and field labels are names.** They identify, in as few words as scan cleanly, and
they do not explain:

| Instead of | Write |
|---|---|
| A column headed "Is it retried?" | A column headed "Retried" |
| A field labelled "Why is this deprecated?" | A field labelled "Reason" |
| A label carrying its own explanation | The noun, with the explanation in the cell beneath |

**Section headings are different, and the opposite advice often applies.** A reader arrives at a
reference page holding a question, and scans headings for the one that matches it. A heading phrased
as that question is frequently the most findable form:

```text
Weaker: Retry conditions          Stronger: What triggers a retry
Weaker: Blocking behavior         Stronger: How long a failing call blocks
```

Under a "Common mistakes" section, a heading that states the whole mistake — "Calling with
`attempts=0` raises `TypeError` and never calls `fn`" — beats a noun phrase, because the reader is
scanning for their symptom rather than for a category.

Use a noun phrase where the section names a contract the reader looks up (`Parameters`,
`Return value and exceptions`). Use the reader's question where the section answers one. Do not
convert a findable question into a tidy noun and lose the reader.

## Write about what exists, in the present

Google's guidance on timeless documentation is explicit: time-sensitive language costs accuracy and
longevity, and words like "now" or "new" become outdated quickly. Applied to a page:

- Describe current behavior in the present tense. `retry` **retries**, not "will retry".
- Delete "currently", "at present", "recently", "new in this version" **from claims about
  behavior**. Version-bound facts belong in a version or compatibility field, where they can be
  checked. This does not govern a statement recording when a check was performed — "verified against
  `retry.py` as it currently stands, on CPython 3.14.6" is provenance, and dating it is the point.
- Do not promise. "Support is planned" is a roadmap claim a reference page cannot verify and should
  not carry.
- Do not narrate the past. "This used to work differently" belongs in a changelog.

## Name the actor

Google's active-voice guidance holds that passive constructions make it hard to see who is
responsible for an action. In technical documentation the actor is usually the exact fact the reader
needs.

```text
Bad:  The exception is re-raised after the attempts are exhausted.
Good: retry re-raises the last ConnectionError after the final attempt.

Bad:  The value is stored and read elsewhere.
Good: main() parses verbose from argv; only _announcing reads it.
```

Passive voice is correct where the actor is genuinely irrelevant or unknown — "the file is created
with mode 0644" is fine when nothing turns on which component created it.

## Match the register to the reader, and do not import a product voice

Reference and troubleshooting pages are dense and factual. A tutorial may be warmer and slower,
because a learner needs orientation a reference reader does not.

Consumer-product style guidance — write like you speak, use contractions, project friendliness — is
written for interface text and marketing surfaces. It does not transfer to a contract page. A
reference that chats costs the scanning reader time and buys nothing.

Whatever register a page takes, hold it for the whole page. A document that opens friendly and turns
terse reads as two documents.

## Delete these on sight

Each of these survives a first draft and says nothing.

| Pattern | Why it fails | Instead |
|---|---|---|
| Hedging — "appears to", "should generally", "it seems" | The reader cannot tell verified from guessed | State what was verified, or mark the claim unverified |
| Minimizers — "simply", "just", "easily", "of course" | Adds no recovery information and understates difficulty | Delete the word |
| Marketing adjectives — "powerful", "seamless", "robust", "smart" | Says nothing to someone doing the task | Delete the clause |
| Unchosen first person — "we recommend", "our API" | Invents a speaker the rest of the docs do not have | A factual statement, or the product's defined voice |
| Anthropomorphism — "the client wants", "the worker tries to" | Hides the mechanism behind an intention | Say what it does, and under what condition |
| "Note that", "It should be noted that", "Please be aware" | Pure preamble | Keep the fact, drop the frame |
| A paragraph opening on "This" or "It" | The referent is one line up and already ambiguous | Name the thing |
| "See the documentation for details" | The reader is in the documentation | Link the exact page or state the fact |

## Read it once as the person who is not you

Two passes, both cheap:

**The fortieth-time pass.** Read as the engineer who has hit this page forty times and needs one
fact at 2 AM. Can they find the contract without reading prose? If the answer requires reading a
paragraph, the fact belongs in a table, a signature, or a heading.

**The first-time pass.** Read as someone who has never seen the system. Is every term either
obvious, defined on the page, or linked? Does the page assume a shape of the codebase they cannot
see?

A page that passes both is finished. A page that passes only the second is a tutorial wearing a
reference's title.
