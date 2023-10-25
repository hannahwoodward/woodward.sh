---
title: 'Habitability metric (OACD)'
enabled: true
post_date: 2023-09-28
---

## A new metric for assessing planetary surface habitability

### & application to tidally-locked exoplanets

Hannah Woodward, Birkbeck
---
## Introduction

- Tidally-locked (TL): one hemisphere in permanent day, one in permanent night - like our moon!
- Most rocky planets in our Galaxy are likely tidally-locked
- Considering 'Habitable Zone' around stars is based on global mean temperatures => not appropriate for TL planets
- 'High proportion' of surface habitability => more detectable biosignatures? => prioritise in observational research
---
## Motivation

- Design a measure of surface habitability that can be applied universally based on:
  - known temperature limits of life (including microbial!)
  - water availability
- Habitable Zone still useful for finding 'approximate' habitability of a planet, but can now start to think about how likely that planet may be to host life or show biosignatures
<!--
- Many papers that consider surface habitability only consider 'complex' or human life...
  - but our own biosignatures originate from microbial life which exist outside of  commonly applied (0-50°C) limits
- Common simplifications used include 'aquaplanets' and then assume a global water availability, but on Earth there are large parts of the ocean with a low density of life! -->
---
## A new surface habitability metric

- Temperature range ($T_s$ surface air temperature):
  - "microbial" life: $-20 \text{°C} \leq T_s \leq 122 \text{°C}$
  - "complex" life: $0 \text{°C} \leq T_s \leq 50 \text{°C}$
- Water availability ($P$ precipitation, $E$ evaporation):
  - $P - E \geq 0$
    - Even if modelling a slab ocean aquaplanet, can use water fluxes to
consider where life might thrive
  - $P \geq 250 \text{ mm}\text{ year}^{-1} \approx 8 \times 10^{-6} \text{ mm}\text{ s}^{-1}$
    - Earth desert definition - can't have E > P on land!
---
## How habitable is Earth?

<div style="max-width:880px; margin: 0 auto">
  <img src="/static/uploads/slides/2023-apex-hab-metric/apex-earth-hab-1.png" alt="Earth habitable area">
  <img src="/static/uploads/slides/2023-apex-hab-metric/apex-earth-hab-2.png" alt="Earth habitable area comparison">
</div>

- Summed: microbial 53%, complex 42%
---
## Earth habitability: Aquaplanet™ edition

<div style="max-width: 880px; margin: 0 auto">
  <img src="/static/uploads/slides/2023-apex-hab-metric/apex-earth-aqua-hab.png" alt="Earth aquaplanet habitable area">
</div>

- How do continents affect Earth's habitability?
- Summed:
  - Slab ocean: microbial 21%, complex 7%
  - Dynamic ocean: microbial 56%, complex 43% (< 3% diff!)
---
## Tidally-locked planets setup

- Two GCMs: ExoCAM & ROCKE-3D
- Dry land 'desert' planet and slab ocean aquaplanet each modelled:
  - "Earth-like" in mass, radius, atmospheric composition (~1 bar $N_2$ + 400ppm $CO_2$)
  - Metric temperature limits applied to land planets
  - Full metric applied to aquaplanets
- Orbital period 4.25 days ~ inner Habitable Zone edge for a low mass star
---
## Tidally-locked desert planet

<div style="max-width: 600px; margin: 0 auto">
  <img src="/static/uploads/slides/2023-oacd-hab-metric/oacd-land-hab.png" alt="Land planets habitability">
</div>

- "Terminator" complex habitability
- ExoCAM: microbial 37%, complex 22%
- ROCKE-3D: microbial 39%, complex 22%
---
## Tidally-locked aquaplanet

<div style="max-width: 880px; margin: 0 auto">
  <img src="/static/uploads/slides/2023-oacd-hab-metric/oacd-aqua-hab.png" alt="Land planets habitability">
</div>

- ExoCAM: microbial 67%, complex 66%
- ROCKE-3D: microbial 65%, complex 35%
---
## Summary

- Defined a new habitability metric based on temperature + water fluxes
  - Qualitatively matches patterns of primary productivity on Earth
  - Aquaplanet Earth habitability sensitive to model setup (e.g. ocean circulation)
    - But dynamic ocean is similar to continental Earth!
- Applied to tidally-locked planets:
  - "Terminator" habitable area on desert worlds
  - A new "Pacman" habitable area on ocean worlds
---
## Future work

- Metric:
  - Explore nutrient availability
  - Explore other datasets to represent Earth life
- Projects:
  - Continue running simulations along inner HZ
  - Effect of changing continental configuration on surface habitability (e.g. Earth climate for previous geological periods)
