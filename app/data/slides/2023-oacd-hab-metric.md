---
title: 'Habitability metric (OACD)'
enabled: true
post_date: 2023-09-28
---

## A new metric for assessing planetary habitability

### & application to tidally-locked exoplanets

Hannah Woodward
---
## Introduction

- Tidally-locked planet: one hemisphere in permanent day, one in permanent night
- Most rocky planets in Galaxy are likely tidally-locked
- Considering 'Habitable Zone' around stars is based on global mean temperatures => not appropriate for TL planets
- Planets with 'high proportion' of surface habitability may be more likely to show detectable biosignatures (evidence of life)
- Considering surface habitability would allow us to include, exclude, or prioritise a large sample within observational research
---
## Motivation

- Design a measure of surface habitability based on known limits of life that can be applied universally
- Many papers that consider surface habitability only consider 'complex' or human life...
  - but our own biosignatures originate from microbial life which exist outside of  commonly applied (0-50°C) limits
- Common simplifications used include 'aquaplanets' and then assume a global water availability, but on Earth there are large parts of the ocean with a low density of life!
- Habitable Zone still useful in finding approximate habitability of a planet based on distance from star, but can now start to think about how likely that planet may be to host life or show biosignatures
---
## A new surface habitability metric

- Temperature range:
  - "microbial" life (-20-122°C)
  - "complex" life (0-50°C)
- Water availability: $P - E \geq 0$
  - Even if modelling a slab ocean aquaplanet, can use water fluxes to
consider where life might thrive
  - Continental configuration & orography implicitly included
---
## How habitable is Earth?

<div style="max-width:880px; margin: 0 auto">
  <img src="/static/uploads/slides/2023-oacd-hab-metric/oacd-earth-hab-1.png" alt="Earth habitable area">
  <img src="/static/uploads/slides/2023-oacd-hab-metric/oacd-earth-hab-2.png" alt="Earth habitable area">
</div>

- Summed: microbial 55%, complex 42%
- **Aside:** let me know if you know of a good dataset!
---
## Tidally-locked planets setup

- Two GCMs: ExoCAM & ROCKE-3D
- Dry land 'desert' planet and slab ocean aquaplanet each modelled:
  - "Earth-like" in mass, radius, atmospheric composition (~1 bar $N_2$ + 400ppm $CO_2$)
  - Metric temperature limits applied to land planets
  - Full metric applied to aquaplanets
- Orbital period ~4.25 days, which lies along inner Habitable Zone edge for a low mass star
---
## Desert planet

<div style="max-width: 760px; margin: 0 auto">
  <img src="/static/uploads/slides/2023-oacd-hab-metric/oacd-land-hab.png" alt="Land planets habitability">
</div>

- ExoCAM: microbial 37%, complex 22%
- ROCKE-3D: microbial 39%, complex 22%
---
## Aquaplanet

<div style="max-width: 880px; margin: 0 auto">
  <img src="/static/uploads/slides/2023-oacd-hab-metric/oacd-aqua-hab.png" alt="Land planets habitability">
</div>

- ExoCAM: microbial 67%, complex 66%
- ROCKE-3D: microbial 65%, complex 35%
---
## Nutrient availability & Ekman transport

- Wind-driven ocean currents at a right angle to wind stress
- Use wind stresses to find regions of up/downwelling without modelling ocean circulation
- Ekman pumping: $w_{Ekman} = \frac{1}{\rho_{0}} \nabla \times \frac{\underline{\tau}}{f}$
- How to integrate within metric?
---
## Ekman pumping on aqua planets

<img src="/static/uploads/slides/2023-oacd-hab-metric/oacd-aqua-ekman.png" alt="Ekman pumping">

- Equatorial patterns similar: bands subtropical winds
  - Large downwelling on day-side, with upwelling along rest of equator
- ROCKE-3D shows strong polar winds => slightly increased downwelling at poles
---
## Summary

- Defined a new habitability metric based on temperature + water fluxes
  - Qualitatively matches patterns of primary productivity on Earth
- Applied to tidally-locked planets:
  - "Terminator" habitable area on desert worlds
  - A new "Pacman" habitable area on ocean worlds
---
## Future work

- Metric:
  - Incorporate nutrient availability?
  - Compare with Earth thermal indexes (e.g. humidex, heat index)
- Projects:
  - Continue running models, incorporate UM + LMD
  - Earth as an aquaplanet?
  - Effect of continental configuration + orography on surface habitability
