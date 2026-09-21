import Std
import Std.Tactic.Omega

namespace Formal

/--
The countable successor map used by the PNCS/GREMLIN FSI.05 seam.
This formalizes only the index/order structure shared with the unilateral shift.
It does not identify an IDT history with a Hilbert space and does not formalize
the Fredholm-index theorem.
-/
def successorShift (k n : Nat) : Nat := n + k

theorem successorShift_injective (k : Nat) :
    Function.Injective (successorShift k) := by
  intro a b h
  exact Nat.add_right_cancel h

theorem successorShift_monotone (k : Nat) :
    Monotone (successorShift k) := by
  intro a b h
  exact Nat.add_le_add_right h k

theorem successorShift_strictMono (k : Nat) :
    StrictMono (successorShift k) := by
  intro a b h
  exact Nat.add_lt_add_right h k

theorem initialIndex_not_in_successorRange
    (k i : Nat) (h : i < k) :
    ¬ ∃ n : Nat, successorShift k n = i := by
  rintro ⟨n, hn⟩
  simp [successorShift] at hn
  omega

theorem successorShift_zero (n : Nat) :
    successorShift 0 n = n := by
  simp [successorShift]

end Formal
