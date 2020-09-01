using Chemicals
using Documenter

makedocs(;
    modules=[Chemicals],
    authors="longemen3000 <longemen3000@gmail.com> and contributors",
    repo="https://github.com/longemen3000/Chemicals.jl/blob/{commit}{path}#L{line}",
    sitename="Chemicals.jl",
    format=Documenter.HTML(;
        prettyurls=get(ENV, "CI", "false") == "true",
        canonical="https://longemen3000.github.io/Chemicals.jl",
        assets=String[],
    ),
    pages=[
        "Home" => "index.md",
    ],
)

deploydocs(;
    repo="github.com/longemen3000/Chemicals.jl",
)
