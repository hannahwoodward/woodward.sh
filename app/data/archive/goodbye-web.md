---
title: 'Goodbye, web'
enabled: true
post_date: 2021-09-02
summary: >
  Why I'm leaving my job in the web & marketing industry.
---

It's been a good run - just under 10 years from the first website I made at uni, in return for a crate of beer. I've learnt so much along the way, but I just don't feel the same excitement I once did when building the fun little websites for uni societies, campaigns, and festivals. It's taken a few years for me to make this decision of what to do next. Learning new web technologies, changing jobs, trying out remote working; whilst it was fun to try out these things and keep learning, the excitement always waned eventually. On deciding to change careers, I've taken the time to reflect upon my experience as a web developer.


## Burn-out

There's a lot of talk of burn-out in the tech world, but it comes as no real surprise when the leading companies like Facebook have an ethos of "move fast and break things". Specifically in web, there seems to be a new trending framework almost every month that just _has_ to be tried out. Given the R&D time and some supposed benefit, I've always been happy to try these out. But often they seem to end up being "trialled in production" before the new tech (and supposed benefits) are properly understood, with no regard as to whether that project is a good use-case, and of course, under time and budget constraints. This results in many over-budget, over-engineered, bug-ridden projects which are a pain to maintain as their setups are so drastically different from each other. It's easy to then see how a company can get trapped in a cycle of "this new framework _has_ to be better than the last", and how developers will inevitably crash from the constant feeling of being behind schedule.


## Complexity

Another issue I've noticed - perhaps partly from prematurely using these new frameworks - is how unnecessarily complex some websites (and their setups) have become. When I first started out with web, there were tools that whilst weren't necessary to build a website, were helpful in the process. An example of this is [Sass](https://sass-lang.com), which helps to write CSS that is readable, maintainable, and re-usable. Now, as CSS has developed over the last few years, it's debatable as to whether the overhead of learning Sass outweighs its benefits, however many agencies still use it without questioning its relevance.

During my time as a developer, the concept of "reactivity" has become fashionable, usually achieved by using heavy and complex JavaScript libraries such as [React](https://reactjs.org) & [Vue](https://vuejs.org). Whilst reactivity certainly has its benefits, these libraries usually require time to learn, understand, and use. As they essentially act as a layer on top of JavaScript, I've noticed that some developers will only learn that specific framework (perhaps via a 2 week intensive bootcamp), but then lack any fundamental understanding of JavaScript (or even programming in general). Combining that with the size and complexity  of these frameworks (almost synonymous to a 'black box'), the codebase then becomes much harder to debug when errors occur. How is the developer to know if it's a problem with their code, the framework, or JavaScript itself?

Static site generation (SSG) is another example of an increasingly popular setup across the web, usually in tandem with a "reactive" library. Having implemented this on a few sites, I've found that my workload has often doubled when performing site updates. Part of this is likely because of the previous issue of having to context switch between projects, but I've also faced other issues, including:

* having to hand-write features that would otherwise be little to no effort to implement on a server-side setup
* having to maintain two codebases (client-side and server-side), each in different languages
* spending significant time "optimising" the SSG configuration
* memory-intensive local development
* long deploy times

Now, there have been advantages to SSG, and I do believe for high-profile sites the advantages probably come out on top, but for a single developer working on relatively small sites, I just can't justify this extra time spent.


## Ads & tracking

There hasn't been a single website that I've made in the last 2 years that hasn't included a tracking script. Facebook and Google services are most commonly used, but there are many others too. Many platforms, such as Shopify or Square, make it easy to integrate these tracking scripts with your website, following a user's journey through a website, tracking clicks, adding to a shopping cart, checking out. On other platforms, I've been asked to manually add this event tracking. In some cases, clients do actually look at this data and analyse it, sometimes with our guidance on how to improve their website. However, this can easily end up with reducing users to "conversions" and implementing dark patterns for increased "engagement" (i.e. purchases). When working on e-commerce projects, I've often wondered if the clients are putting in the same amount of effort on actually improving their product.

We also have to consider that it's not only the client who has access to this data. Google & Facebook are advertising companies and are the ones collecting and owning the data - they're just allowing smaller companies access to that data in the form of "analytics". Even then, there are terms and conditions to this access, with [increasing numbers of people getting locked out of their accounts (sometimes indefinitely)](https://www.businessinsider.com/google-users-locked-out-after-years-2020-10).

When discussing this with friends, I've found that a lot of people don't seem to care about this aggregation of data; I've even heard a few people say that they're happy to receive targeted ads. Whilst I don't agree with the idea of my personal data being collected so I can be sold into yet more consumerism, there are many more issues at hand:

* [The Cambridge Analytica scandal](https://www.bbc.co.uk/news/topics/c81zyn0888lt/facebook-cambridge-analytica-scandal)
* [Hacking of Facebook accounts](https://www.theguardian.com/technology/2018/sep/28/facebook-50-million-user-accounts-security-berach)
* [Data leaks](https://www.hackread.com/facebook-data-users-106-countries-leaked-online/)
* [Increasing requests Governments requesting data](https://about.fb.com/news/2017/04/global-government-requests-report-7/)
* ['Personalised' Instagram ads](https://signal.org/blog/the-instagram-ads-you-will-never-see/)

Even though laws such as GDPR are being introduced, they are always on the back-foot and just aren't making these larger companies accountable in any significant way. Facebook and Google will happily continue with their unethical data harvesting, knowing that that their profits still outweigh any fine they may be given for breaking the law. For smaller web agencies and their clients, it's a case of wading through legal jargon to find out what is and isn't allowed, and who should be held accountable for any data breaches. Finally, for the general user of the web, the end result is just a series of questionably legal pop-ups that just further hinder their experience, and doesn't actually add any additional protection to their data. This also doesn't seem to affect tracking that happens in cases where consent cannot be given, such as in emails or when a user has disabled JavaScript in their browser.

Finally, many of these social media companies are increasingly acting as walled gardens. Over time, API access to such data has been getting increasingly difficult to use or removed entirely. The latest version of the [Instagram API](https://developers.facebook.com/docs/instagram-basic-display-api/) requires a client to have a Facebook account and for them to generate a (short-lived) API key which then needs to be passed on (securely) to the developers. Perhaps this isn't an issue for a large company with an in-house dev team, but I've had many a difficult call with clients trying to guide them through this process, and all in the name of just showing an Instagram feed on their website. On the general web user side of things, expect to have to complete many "anti-bot/spam tasks" (e.g. CAPTCHA) if you have an adblocker enabled or no Facebook account to track you across the internet. Many smaller businesses are also increasingly choosing to use Facebook or Instagram as their primary online presence, with important contact details and opening times hidden away behind a "login wall".


## Environmental impacts

An often unconsidered part of the internet (and computing technology in general perhaps) is its "carbon footprint". Have you ever visited a website which has slowed your device down, drained your battery quickly, or made your computer fans start whirring away? Do you remember the 'overheating' xbox problems (along with the 'towel trick' to cool it down)? I think the first time I truly thought about global energy usage of these things was visiting [CERN](https://home.cern) on a school trip. They showed us their main data centre; essentially a very large room being constantly cooled, filled with stacks of servers. My main takeaway from that trip was the fact that if there are was some catastrophic power failure (including backup power), this room would heat by 1C every second. If I remember correctly, this data centre was also just used internally. Expanding this idea to think about the masses of data centres there are across the world, used by companies, institutions, governments it makes one wonder: how much power are we pumping into these machines and cooling systems globally?

Linking this back to the web, I feel like this ties in quite well with the over-engineering and overcomplexity seen in many modern websites. In particular, the worst culprits I've noticed (both as a web user and as a developer) are the ones with the 'modern' setup of some reactive framework with SSG and numerous tracking scripts. In fact, there is a great resource that [measures the carbon footprint of a website](https://www.websitecarbon.com), which in theory could be useful in guiding agencies and clients to consider this. In reality however, it might be a hard argument to win when many clients already simultaneously want large image/video-heavy, interactive website 'experiences', but also fast loading times (mostly for better SEO). Perhaps in the grand scheme of things, websites aren't such a problem, with Bitcoin [placing in the top 30 energy users (by country) worldwide](https://www.bbc.co.uk/news/technology-56012952), as well as [producing significant amounts of e-waste](https://doi.org/10.1016/j.resconrec.2021.105901).

TODO:

- rare metal usage in devices - https://hir.harvard.edu/not-so-green-technology-the-complicated-legacy-of-rare-earth-mining/
