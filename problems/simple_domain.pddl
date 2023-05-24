(define (domain simple_domain)
    (:requirements:strips :action-costs :fluents)
    (:predicates (at ?x) (adj ?x ?y) )

  (:functions
    (distance ?from ?to)
    (total-cost)
   )
    (:action move
        :parameters (?from ?to)
        :precondition (and(at ?from)(adj ?from ?to))
        :effect (and(not(at ?from))(at ?to)
        (increase (total-cost) (distance ?from ?to)))
    )
)