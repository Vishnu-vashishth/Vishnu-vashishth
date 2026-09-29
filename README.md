<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/main/assets/header-dark.svg" />
  <img alt="Vishnu Vashishth — backend engineer, distributed systems" src="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/main/assets/header-light.svg" width="100%" />
</picture>

<br/>

I spend most of my time in the unglamorous half of the stack — the part that has to be correct at 3am.

Lately that means **payment infrastructure**: idempotent checkout flows, provider webhooks that survive being delivered twice or not at all, subscription lifecycles that don't drift, and event delivery between services that can't afford to drop a message. Before that, a lot of Node, a lot of MongoDB query plans, and a real appreciation for observability that answers questions someone actually asked.

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/main/assets/stats-dark.svg" />
  <img alt="GitHub activity" src="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/main/assets/stats-light.svg" width="100%" />
</picture>

<br/>

## Currently

<details open>
<summary><b>A payment service several products share</b></summary>

<br/>

Rather than letting each product grow its own half-correct Stripe integration, one provider-agnostic service owns checkout for all of them.

- **One provider config, per-app plans** — products differ as data, never as branches in the service
- **Idempotent settlement** — a webhook delivered twice settles once; a webhook never delivered gets recovered
- **gRPC contracts** between the payment service and the apps that consume it
- **Subscription lifecycles** — renewals, one-time-payment upgrades, grace periods

</details>

<details>
<summary><b>Backends for AI chat platforms</b></summary>

<br/>

Character-driven chat products: conversation state, suggestion generation, prompt plumbing, and the migrations that keep years of message history honest — at a collection size where query plans stop being academic.

</details>

<details>
<summary><b>Observability that earns its keep</b></summary>

<br/>

Structured logs to Axiom, dashboards built around real questions, and feature flags so a rollout is a decision rather than a deploy.

</details>

<br/>

## Stack

|  |  |
| :-- | :-- |
| **Languages** | TypeScript · JavaScript · Python |
| **Backend** | NestJS · Node.js · gRPC · Protocol Buffers |
| **Data** | MongoDB · Mongoose · Redis · Typesense |
| **Cloud** | AWS — SQS, S3, KMS, Secrets Manager, Firehose · Docker |
| **Payments** | Stripe · PayPal |
| **Tooling** | GitHub Actions · Jest · Axiom · GrowthBook |

<br/>

<!-- Contribution graph — hidden for now.
     Your public contribution graph shows ~4 contributions, because the work lives in
     private org repos. Turn on Settings → Public profile → "Include private
     contributions on my profile", then delete these comment markers to show it.

## Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/output/github-snake-dark.svg" />
  <img alt="Contribution graph" src="https://raw.githubusercontent.com/Vishnu-vashishth/Vishnu-vashishth/output/github-snake.svg" width="100%" />
</picture>

-->

<br/>

---

<sub>
Open to conversations about backend architecture, payments, or anything that has to stay up —
<a href="mailto:vishnuvashisth31273@gmail.com">vishnuvashisth31273@gmail.com</a>
<!-- LinkedIn: paste your URL and uncomment → · <a href="https://www.linkedin.com/in/YOUR-HANDLE/">LinkedIn</a> -->
</sub>
